#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3指標統合分析スクリプト（完全版）
気圧・湿度・日照データを統合し、総合スコアリング・統計検定を実施
NASA POWER APIから取得した正確な日照データを使用
"""

import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("=" * 80)
print("3指標統合分析（完全版） - 頭痛患者に最適な移住先ランキング")
print(f"開始時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# =============================================================================
# 1. データ読み込み
# =============================================================================
print("\n【ステップ1】データ読み込み中...")

# 気圧データ
print("  - 気圧データ読み込み...")
pressure_complete = pd.read_csv('/home/ec2-user/hirashimallc/23_pj-blog/outputs/pressure_49regions_complete.csv')

# 湿度データ（国内）
print("  - 湿度データ（国内）読み込み...")
humidity_jp = pd.read_csv('/home/ec2-user/hirashimallc/23_pj-blog/outputs/humidity_47prefs.csv')

# 湿度データ（国際）
print("  - 湿度データ（国際）読み込み...")
humidity_intl = pd.read_csv('/home/ec2-user/hirashimallc/23_pj-blog/outputs/humidity_international.csv')

# 日照データ（国内）
print("  - 日照データ（国内）読み込み...")
sunshine_jp = pd.read_csv('/home/ec2-user/hirashimallc/23_pj-blog/outputs/sunshine_47prefs.csv')

# 日照データ（国際 - NASA POWER）
print("  - 日照データ（国際 - NASA POWER）読み込み...")
sunshine_intl_nasa = pd.read_csv('/home/ec2-user/hirashimallc/23_pj-blog/outputs/sunshine_international_nasa_power.csv')

print(f"\n✓ データ読み込み完了")
print(f"  気圧: {len(pressure_complete)}件")
print(f"  湿度（国内）: {len(humidity_jp)}件")
print(f"  湿度（国際）: {len(humidity_intl)}件")
print(f"  日照（国内）: {len(sunshine_jp)}件")
print(f"  日照（国際 - NASA POWER）: {len(sunshine_intl_nasa)}件")

# =============================================================================
# 2. 地域名マッピング（国内 & 国際統一）
# =============================================================================
print("\n【ステップ2】地域名統一処理...")

# 気圧データの地域名カラム確認
if '都道府県' in pressure_complete.columns:
    pressure_complete = pressure_complete.rename(columns={'都道府県': '地域名'})
elif '地域' in pressure_complete.columns:
    pressure_complete = pressure_complete.rename(columns={'地域': '地域名'})
elif '都市' in pressure_complete.columns:
    pressure_complete = pressure_complete.rename(columns={'都市': '地域名'})

# 湿度データ（国内）
if '都道府県' in humidity_jp.columns:
    humidity_jp = humidity_jp.rename(columns={'都道府県': '地域名'})

# 湿度データ（国際）
if '都市' in humidity_intl.columns:
    humidity_intl = humidity_intl.rename(columns={'都市': '地域名'})

# 日照データ（国内）
if '都道府県' in sunshine_jp.columns:
    sunshine_jp = sunshine_jp.rename(columns={'都道府県': '地域名'})

# 日照データ（国際 - NASA POWER）
if '都市' in sunshine_intl_nasa.columns:
    sunshine_intl_nasa = sunshine_intl_nasa.rename(columns={'都市': '地域名'})

print("✓ 地域名カラム統一完了")

# =============================================================================
# 3. 地域別統計量の算出
# =============================================================================
print("\n【ステップ3】地域別統計量算出...")

# 気圧の統計量（日較差を使用）
print("  - 気圧統計量算出中...")
pressure_stats = pressure_complete.groupby('地域名')['日較差_hPa'].agg([
    ('気圧日較差_平均', 'mean'),
    ('気圧日較差_標準偏差', 'std'),
    ('気圧日較差_最大', 'max'),
    ('気圧日較差_最小', 'min')
]).reset_index()

# 湿度の統計量（国内 + 国際）
print("  - 湿度統計量算出中...")
humidity_all = pd.concat([humidity_jp, humidity_intl], ignore_index=True)
humidity_stats = humidity_all.groupby('地域名')['平均湿度_%'].agg([
    ('湿度_平均', 'mean'),
    ('湿度_標準偏差', 'std'),
    ('湿度_最大', 'max'),
    ('湿度_最小', 'min')
]).reset_index()

# 日照の統計量（国内 + NASA POWER国際データ）
print("  - 日照統計量算出中...")

# 国内データ処理
sunshine_jp_copy = sunshine_jp.copy()
if '日照時間_h' in sunshine_jp_copy.columns:
    sunshine_jp_copy = sunshine_jp_copy.rename(columns={'日照時間_h': '日照時間統一_h'})

# NASA POWER国際データ処理
sunshine_intl_nasa_copy = sunshine_intl_nasa.copy()
if '推定日照時間_h' in sunshine_intl_nasa_copy.columns:
    sunshine_intl_nasa_copy = sunshine_intl_nasa_copy.rename(columns={'推定日照時間_h': '日照時間統一_h'})

# 統合
sunshine_all = pd.concat([sunshine_jp_copy, sunshine_intl_nasa_copy], ignore_index=True)

sunshine_stats = sunshine_all.groupby('地域名')['日照時間統一_h'].agg([
    ('日照_平均', 'mean'),
    ('日照_標準偏差', 'std'),
    ('日照_最大', 'max'),
    ('日照_最小', 'min')
]).reset_index()

print("✓ 統計量算出完了")

# =============================================================================
# 4. データ統合
# =============================================================================
print("\n【ステップ4】データ統合中...")

# 気圧 + 湿度
integrated = pressure_stats.merge(humidity_stats, on='地域名', how='outer')

# + 日照
integrated = integrated.merge(sunshine_stats, on='地域名', how='outer')

print(f"✓ 統合データ: {len(integrated)}地域")

# 欠損値確認
print("\n欠損値確認:")
print(integrated.isnull().sum())

# =============================================================================
# 5. 正規化スコアリング（0-100スケール）
# =============================================================================
print("\n【ステップ5】正規化スコアリング...")

# 気圧日較差が低いほど良い → 逆スコア
integrated['気圧スコア'] = 100 - (
    (integrated['気圧日較差_平均'] - integrated['気圧日較差_平均'].min()) /
    (integrated['気圧日較差_平均'].max() - integrated['気圧日較差_平均'].min()) * 100
)

# 湿度平均が低いほど良い → 逆スコア
integrated['湿度スコア'] = 100 - (
    (integrated['湿度_平均'] - integrated['湿度_平均'].min()) /
    (integrated['湿度_平均'].max() - integrated['湿度_平均'].min()) * 100
)

# 日照平均が高いほど良い → 正スコア
integrated['日照スコア'] = (
    (integrated['日照_平均'] - integrated['日照_平均'].min()) /
    (integrated['日照_平均'].max() - integrated['日照_平均'].min()) * 100
)

# 総合スコア（重み付け: 気圧40%, 湿度30%, 日照30%）
integrated['総合スコア'] = (
    integrated['気圧スコア'] * 0.40 +
    integrated['湿度スコア'] * 0.30 +
    integrated['日照スコア'] * 0.30
)

# ランキング
integrated = integrated.sort_values('総合スコア', ascending=False).reset_index(drop=True)
integrated['ランク'] = range(1, len(integrated) + 1)

print("✓ スコアリング完了")

# =============================================================================
# 6. 統計検定
# =============================================================================
print("\n【ステップ6】統計検定実施...")

# 相関分析
print("\n■ 相関分析:")
correlation_matrix = integrated[[
    '気圧日較差_平均', '湿度_平均', '日照_平均', '総合スコア'
]].corr()
print(correlation_matrix)

# Pearson相関係数と有意性検定
print("\n■ 各指標と総合スコアのPearson相関係数:")
for col in ['気圧日較差_平均', '湿度_平均', '日照_平均']:
    r, p = stats.pearsonr(integrated[col].dropna(),
                           integrated.loc[integrated[col].notna(), '総合スコア'])
    print(f"  {col} vs 総合スコア: r={r:.3f}, p={p:.6f}")

# 上位10地域 vs 下位10地域の検定
print("\n■ 上位10地域 vs 下位10地域 t検定:")

top10 = integrated.head(10)
bottom10 = integrated.tail(10)

# 気圧日較差の検定
t_stat_pressure, p_val_pressure = stats.ttest_ind(
    top10['気圧日較差_平均'], bottom10['気圧日較差_平均']
)
print(f"  気圧日較差: t={t_stat_pressure:.3f}, p={p_val_pressure:.4f}")

# 湿度平均の検定
t_stat_humidity, p_val_humidity = stats.ttest_ind(
    top10['湿度_平均'], bottom10['湿度_平均']
)
print(f"  湿度平均: t={t_stat_humidity:.3f}, p={p_val_humidity:.4f}")

# 日照平均の検定
t_stat_sunshine, p_val_sunshine = stats.ttest_ind(
    top10['日照_平均'], bottom10['日照_平均']
)
print(f"  日照平均: t={t_stat_sunshine:.3f}, p={p_val_sunshine:.4f}")

print("\n✓ 統計検定完了")

# =============================================================================
# 7. 結果出力
# =============================================================================
print("\n【ステップ7】結果出力...")

# Top 10ランキング表示
print("\n" + "=" * 80)
print("TOP 10 最適移住先ランキング")
print("=" * 80)

for idx, row in integrated.head(10).iterrows():
    print(f"\n【第{row['ランク']}位】 {row['地域名']}")
    print(f"  総合スコア: {row['総合スコア']:.1f}点")
    print(f"  - 気圧スコア: {row['気圧スコア']:.1f}点（日較差: {row['気圧日較差_平均']:.2f}hPa）")
    print(f"  - 湿度スコア: {row['湿度スコア']:.1f}点（平均湿度: {row['湿度_平均']:.1f}%）")
    print(f"  - 日照スコア: {row['日照スコア']:.1f}点（平均日照: {row['日照_平均']:.1f}時間）")

# Bottom 10ランキング表示
print("\n" + "=" * 80)
print("WORST 10 避けるべき地域")
print("=" * 80)

for idx, row in integrated.tail(10).iterrows():
    print(f"\n【第{row['ランク']}位】 {row['地域名']}")
    print(f"  総合スコア: {row['総合スコア']:.1f}点")
    print(f"  - 気圧スコア: {row['気圧スコア']:.1f}点（日較差: {row['気圧日較差_平均']:.2f}hPa）")
    print(f"  - 湿度スコア: {row['湿度スコア']:.1f}点（平均湿度: {row['湿度_平均']:.1f}%）")
    print(f"  - 日照スコア: {row['日照スコア']:.1f}点（平均日照: {row['日照_平均']:.1f}時間）")

# CSV保存
output_file = '/home/ec2-user/hirashimallc/23_pj-blog/outputs/integrated_analysis_3indicators.csv'
integrated.to_csv(output_file, index=False, encoding='utf-8-sig')

print("\n" + "=" * 80)
print("分析完了！")
print("=" * 80)
print(f"終了時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"\n保存先: {output_file}")
print(f"分析地域数: {len(integrated)}地域")
print("=" * 80)
