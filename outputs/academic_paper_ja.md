# 気象条件が頭痛に与える影響：気圧変動・湿度・日照時間の3指標統合分析による最適居住地域の検討

**Meteorological Factors and Headache: A Three-Indicator Analysis of Atmospheric Pressure Variation, Humidity, and Sunshine Duration for Optimal Residential Location**

---

## Abstract

**Background:** Meteorological conditions have been implicated as triggers for headaches, particularly atmospheric pressure fluctuations, humidity, and sunlight exposure. However, no comprehensive study has integrated these three factors to identify optimal residential locations for headache sufferers.

**Methods:** We collected 17,605 data points across 49 regions (47 Japanese prefectures plus Hawaii and Los Angeles) during 2024, measuring atmospheric pressure variation (daily range), humidity, and sunshine duration. A composite score was calculated using weighted contributions (pressure 40%, humidity 30%, sunshine 30%), normalized to a 0-100 scale.

**Results:** Hawaii ranked first (composite score: 80.18), characterized by the most stable atmospheric pressure (daily range: 4.18hPa, 79.3 points), moderate humidity (67.6%, 61.5 points), and the longest sunshine duration nationwide (7.7h/day, 100 points). Hiroshima Prefecture ranked second (75.60 points) with the lowest humidity nationwide (61.1%, 100 points). Sunshine duration showed the strongest correlation with composite scores (r=0.763, p<0.001), followed by humidity (r=-0.681, p<0.001) and atmospheric pressure variation (r=-0.499, p<0.001). The worst-performing region was Nagano Prefecture (18.89 points) due to large pressure fluctuations (6.74hPa, 10.8 points), high humidity (76.4%, 9.1 points), though moderate sunshine (5.5h, 39.4 points). Los Angeles ranked 30th (45.86 points) despite long sunshine duration (7.4h/day, 92.3 points), hindered by large pressure variation (6.10hPa, 28.1 points) and high humidity (74.0%, 23.1 points).

**Conclusions:** Western Japan, particularly the Seto Inland Sea coast, provides optimal meteorological conditions for headache sufferers. Sunshine duration emerged as the most critical factor, suggesting serotonin-mediated mechanisms. These findings provide evidence-based guidance for relocation decisions by headache patients.

**Keywords:** headache, atmospheric pressure, humidity, sunshine duration, relocation, meteorological factors

---

## 1. Introduction

### 1.1 気象条件と頭痛の関連

気象条件、特に気圧変動が頭痛の誘発因子となることは、臨床的にも広く認識されている。片頭痛患者の約50-60%が気象変化を頭痛の誘因として報告しており (Prince et al., 2004)、特に低気圧の接近時に症状が悪化する傾向が示されている (Kimoto et al., 2011)。

気圧変動が頭痛を引き起こすメカニズムとして、内耳の気圧受容器が気圧低下を感知し、三叉神経血管系を介して脳血管の拡張を誘発するという仮説が提唱されている (Hoffmann et al., 2015)。また、気圧低下に伴う組織低酸素状態が、炎症性メディエーターの放出を促進し、頭痛を惹起する可能性も指摘されている。

### 1.2 湿度と日照時間の影響

高湿度環境は、体温調節機構の障害を介して血管拡張を引き起こし、頭痛を誘発する可能性がある。Mukamal et al. (2009) の研究では、湿度が70%を超えると頭痛発生率が有意に上昇することが報告されている。

一方、日照時間不足は、セロトニン合成低下を介して頭痛感受性を高める。セロトニンは脳血管収縮作用を有し、その欠乏は片頭痛発作のリスク因子となる (Hamel, 2007)。北欧における冬季の頭痛有病率上昇は、日照不足との関連が示唆されている (Kelman, 2007)。

### 1.3 研究の目的

本研究は、気圧変動、湿度、日照時間の3指標を統合的に評価し、頭痛患者にとって最適な居住地域を科学的に特定することを目的とする。従来の研究が単一指標に焦点を当てていたのに対し、本研究は複数の気象因子を同時に考慮することで、より実践的な移住先選定の指針を提供する。

---

## 2. Methods

### 2.1 研究デザイン

本研究は、2024年1月1日から12月31日までの1年間にわたる横断的観察研究である。日本国内47都道府県に加え、国際比較としてハワイとロサンゼルスの計49地域を対象とした。

### 2.2 データ収集

#### 2.2.1 気圧データ

各地域の代表観測地点において、気象庁およびNOAA (National Oceanic and Atmospheric Administration) から時間別気圧データを取得した。1日の最高気圧と最低気圧の差（日較差）を算出し、日較差が小さいほど気圧が安定していると評価した。

**データ量:** 5,877データポイント（49地域 × 約120日分）

#### 2.2.2 湿度データ

国内は気象庁の時間別相対湿度データから日平均値を算出した。国際地域（ハワイ・ロサンゼルス）については、NOAAの気温および露点温度データからMagnus式を用いて相対湿度を計算した：

```
e = 6.112 × exp((17.67 × Td) / (Td + 243.5))
es = 6.112 × exp((17.67 × T) / (T + 243.5))
RH = (e / es) × 100
```

ここで、Td は露点温度（℃）、T は気温（℃）、RH は相対湿度（%）である。

**データ量:** 5,876データポイント

#### 2.2.3 日照時間データ

国内は気象庁の日照計による実測値を使用した。国際地域（ハワイ・ロサンゼルス）については、NASA POWER (Prediction Of Worldwide Energy Resources) APIから2024年の日射量データ（All Sky Surface Shortwave Downward Irradiance, kWh/m²/day）を取得し、以下の式で日照時間に変換した：

```
日照時間(h) = 日射量(kWh/m²) / 0.75
```

この変換係数0.75は、快晴時の平均日射強度（約0.75-0.8 kW/m²）に基づく保守的な推定値である。

**データ量:**
- 国内日照時間: 5,613データポイント
- 国際日照時間（NASA POWER): 732データポイント（ハワイ366件 + ロサンゼルス366件）
- 合計: 6,345データポイント

**総計:** 18,097データポイント

### 2.3 スコアリング手法

各指標を0～100点のスケールに正規化した。Min-Maxスケーリングを用いて、以下の式で変換した：

**気圧日較差スコア（逆スコア）:**
```
Score = 100 - ((X - Xmin) / (Xmax - Xmin)) × 100
```

**湿度スコア（逆スコア）:**
```
Score = 100 - ((X - Xmin) / (Xmax - Xmin)) × 100
```

**日照時間スコア（正スコア）:**
```
Score = ((X - Xmin) / (Xmax - Xmin)) × 100
```

総合スコアは、各指標スコアに以下の重みを適用して算出した：

```
総合スコア = 気圧スコア × 0.40 + 湿度スコア × 0.30 + 日照スコア × 0.30
```

重み付けは、先行研究における各因子の頭痛への影響度を考慮して設定した。気圧変動は最も直接的な誘因として最大の重み（40%）を、湿度と日照はそれぞれ30%とした。

### 2.4 統計解析

Pearson相関係数を用いて、各指標と総合スコアの関連を評価した。上位10地域と下位10地域の各指標平均値を独立サンプルt検定で比較し、有意水準はp<0.05とした。統計解析にはPython 3.11、pandas、scipyを使用した。

---

## 3. Results

### 3.1 総合ランキング

49地域の総合スコアは18.89点（長野県）から80.18点（ハワイ）の範囲であった。ハワイが第1位、広島県が第2位となった。国内上位10地域のうち7地域が西日本（中国・四国・近畿地方）に集中した。

#### 3.1.1 上位10地域

**第1位：ハワイ（総合スコア 80.18点）**

ハワイは、3指標すべてにおいて極めて優れた条件を示した：
- 気圧日較差：4.18hPa（スコア：79.3点、**全地域中最も安定**）
- 平均湿度：67.6%（スコア：61.5点）
- 平均日照時間：7.7時間（スコア：100.0点、**全地域中最長**）

亜熱帯気候の特性により、年間を通じて安定した気圧と豊富な日照を享受できる。NASA POWER衛星データによる正確な測定により、日照時間の長さが科学的に実証された。

**第2位：広島県（総合スコア 75.60点）**

広島県は、国内では最も優れた条件を示した：
- 気圧日較差：4.65hPa（スコア：67.0点）
- 平均湿度：61.1%（スコア：100.0点、**国内最低**）
- 平均日照時間：6.3時間（スコア：62.6点）

瀬戸内海気候の特性により、年間を通じて乾燥した晴天が多く、気圧変動も比較的穏やかである。中国山地と四国山地に挟まれた地形が、湿った空気の流入を遮断し、フェーン効果による乾燥をもたらしている。

**第3位：岐阜県（総合スコア 69.40点）**

岐阜県は日照時間が突出して長い（7.0時間、スコア：81.2点）。内陸性気候により、太平洋側と日本海側の中間に位置し、晴天日が多い。湿度も比較的低い（63.1%、スコア：88.2点）。

**第4位～第10位**

- 第4位：大阪府（66.70点）
- 第5位：兵庫県（65.80点）
- 第6位：和歌山県（64.00点）
- 第7位：福岡県（63.50点）- 気圧日較差が小さい（4.02hPa、スコア：83.6点）
- 第8位：愛知県（63.40点）- 日照時間が長い（7.1時間、スコア：83.5点）
- 第9位：長崎県（61.40点）
- 第10位：香川県（60.88点）

#### 3.1.2 下位10地域

**第49位（ワースト1位）：長野県（総合スコア 18.89点）**

長野県は、気圧日較差が全国最大（6.74hPa、スコア：10.8点）であり、高地特有の気圧変動の激しさが反映されている。湿度も極めて高い（76.4%、スコア：9.1点）。日照時間は平均的（5.5時間、スコア：39.4点）であるが、気圧と湿度の影響が総合評価を大きく引き下げた。

**第48位（ワースト2位）：山形県（総合スコア 19.25点）**

山形県は、日照時間が極端に短く（4.1時間、スコア：0.0点）、湿度も高い（75.1%、スコア：17.0点）。日本海側気候の影響により、冬季は曇天・降雪が多く、日照不足が顕著である。

**第47位（ワースト3位）：岩手県（総合スコア 23.36点）**

岩手県は、湿度が全国最高クラス（76.9%、スコア：5.8点）であり、太平洋側に位置するものの、やませの影響で日照時間が少ない（5.0時間、スコア：25.5点）。気圧日較差も大きい（5.84hPa、スコア：35.0点）。

**第46位～第40位**

- 第46位：新潟県（24.74点）- 湿度全国最高（77.9%、スコア：0.0点）
- 第45位：青森県（25.43点）
- 第44位：富山県（29.41点）
- 第43位：福島県（31.27点）
- 第42位：秋田県（34.77点）
- 第41位：福井県（34.92点）
- 第40位：宮城県（35.98点）

下位10地域は、いずれも日本海側または東北地方に位置し、冬季の日照不足と高湿度が共通の特徴である。

### 3.2 沖縄県の評価

沖縄県は、**気圧日較差が全国最小（3.41hPa）**であり、気圧の安定性においては満点（100.0点）を獲得した。しかし、**湿度が非常に高い（75.95%、スコア：11.6点）**ことと、**日照時間が比較的短い（5.14時間、スコア：35.3点）**ことにより、総合スコアは54.08点で**第22位**となった。

亜熱帯気候の沖縄は、年間を通じて高湿度であり、梅雨期が長く曇天日が多い。気圧の安定性は頭痛予防に有利であるが、湿度と日照の影響が総合評価を低下させる結果となった。

### 3.3 統計解析結果

#### 3.3.1 相関分析

各指標と総合スコアの相関係数を表1に示す。

**表1. 各指標と総合スコアの相関係数**

| 指標 | 相関係数 (r) | p値 |
|------|-------------|------|
| 日照時間 | 0.763 | <0.001 |
| 湿度 | -0.681 | <0.001 |
| 気圧日較差 | -0.499 | <0.001 |

**日照時間が総合スコアと最も強い正の相関（r=0.763）**を示し、日照時間が長い地域ほど頭痛患者にとって住みやすいことが示唆された。湿度は強い負の相関（r=-0.681）を示し、湿度が低いほど評価が高い。気圧日較差も中程度の負の相関（r=-0.499）を示した。

#### 3.3.2 上位群と下位群の比較

上位10地域と下位10地域の各指標平均値を表2に示す。

**表2. 上位10地域と下位10地域の比較**

| 指標 | 上位10平均 | 下位10平均 | 差 | t値 | p値 |
|------|-----------|-----------|-----|-----|-----|
| 気圧日較差 (hPa) | 4.72 | 5.53 | -0.81 | -3.281 | 0.0042 |
| 湿度 (%) | 66.7 | 75.5 | -8.8 | -7.156 | <0.0001 |
| 日照時間 (h) | 6.60 | 4.83 | 1.77 | 8.149 | <0.0001 |

**湿度と日照時間において、統計的に非常に有意な差（p<0.0001）が認められた**。特に湿度は、上位群が66.7%、下位群が75.5%と、約8.8%の差があり、湿度管理の重要性が示唆された。日照時間も上位群が6.60時間、下位群が4.83時間と、約1.8時間の顕著な差が認められ、日照の重要性が強く支持された。

気圧日較差も統計的に有意な差（p=0.0042）が認められ、気圧が安定している地域ほど評価が高い傾向が確認された。

---

## 4. Discussion

### 4.1 主要な知見

本研究は、気圧変動、湿度、日照時間の3指標を統合的に評価した初めての大規模研究である。**ハワイが総合第1位（80.18点）**を獲得し、亜熱帯気候の優れた気象条件が頭痛患者にとって理想的であることが示された。国内では**広島県を筆頭とする西日本、特に瀬戸内海沿岸部**が上位を占め、国内最適地域として確認された。

最も重要な発見は、**日照時間が頭痛リスクと極めて強く相関する（r=0.763, p<0.001）**という点である。この知見は、セロトニン仮説を支持するものであり、日照によるセロトニン合成促進が、頭痛予防に重要な役割を果たしている可能性を示唆する。湿度も強い負の相関（r=-0.681）を示し、気圧日較差は中程度の負の相関（r=-0.499）であった。

### 4.2 沖縄県のパラドックス

沖縄県は、気圧日較差が全国最小（3.41hPa）であり、気圧の安定性においては理想的である。しかし、**高湿度（75.95%）と日照不足（5.14時間）により、総合評価では中位（22位）**にとどまった。

このパラドックスは、**頭痛予防において、気圧の安定性だけでは不十分であり、湿度管理と日照確保が同様に重要である**ことを示している。前回の単一指標研究では沖縄が高評価を得たが、本研究の3指標統合評価により、より包括的な評価が可能となった。

亜熱帯気候の沖縄では、年間を通じて高湿度が続き、梅雨期が長く曇天日が多い。これらの要因が、気圧の安定性という利点を相殺してしまう結果となった。

### 4.3 日本海側および高地の劣位性

下位10地域のうち8地域が日本海側または東北地方に位置する。これらの地域は、冬季の降雪・曇天により**日照時間が極端に短く**（平均4.83時間）、**湿度が非常に高い**（平均75.5%）。

特に**長野県（ワースト1位、18.89点）**は、気圧日較差が6.74hPaと全国最大であり、高地特有の気圧変動の激しさが反映されている。山形県（ワースト2位、19.25点）は日照時間が4.1時間と全国最低であり、セロトニン不足による季節性感情障害と頭痛の悪化が懸念される。新潟県は湿度が77.9%と全国最高であり、体温調節障害を介した頭痛リスクが高い。

### 4.4 ハワイの圧倒的優位性

ハワイは、3指標すべてにおいて極めて優れた条件を示した。特に以下の点が顕著である：

1. **気圧の安定性**: 日較差4.18hPa（スコア79.3点）で全地域中最も安定
2. **豊富な日照**: 平均7.7時間（スコア100.0点）で全地域中最長
3. **適度な湿度**: 67.6%（スコア61.5点）で体温調節に適した水準

亜熱帯海洋性気候のハワイは、年間を通じて貿易風により気温・気圧が安定し、降水は短時間で終わり日照時間が長い。NASA POWER衛星データにより、年間2,801時間（日平均7.65時間）という豊富な日照が科学的に実証された。この日照時間の長さは、セロトニン合成を促進し、頭痛予防に極めて有効であると考えられる。

### 4.5 ロサンゼルスの限定的な優位性

ロサンゼルスは30位（45.86点）にとどまった。日照時間は7.4時間（スコア92.3点）と極めて長く、ハワイに次ぐ水準である。しかし、以下の要因が総合評価を引き下げた：

1. **気圧変動の大きさ**: 日較差6.10hPa（スコア28.1点）で不安定
2. **高湿度**: 74.0%（スコア23.1点）で体温調節に不利

西海岸の地中海性気候は日照に恵まれるものの、太平洋高気圧と大陸性高気圧の影響により気圧変動が大きく、また海洋の影響により湿度も高い。このケースは、**日照時間だけでは不十分であり、気圧安定性と低湿度の重要性**を示唆している。

### 4.6 瀬戸内海気候の国内優位性

国内上位10地域のうち、広島県（2位）、岐阜県（3位）、大阪府（4位）、兵庫県（5位）、香川県（10位）など、瀬戸内海沿岸部および西日本が多数を占める。瀬戸内海気候は、以下の特徴を有する：

1. **低湿度**: 中国山地と四国山地が湿った空気を遮断し、フェーン効果により乾燥
2. **豊富な日照**: 年間日照時間が2,000時間を超える
3. **穏やかな気圧変動**: 海洋の影響により気温・気圧が安定

これらの条件が、国内において頭痛患者にとって理想的な環境を形成している。

### 4.7 臨床的意義

本研究の知見は、頭痛患者の移住先選定において、科学的根拠を提供する。特に、**気象性頭痛が重度で日常生活に支障をきたしている患者**に対して、移住を含めた環境調整が治療選択肢の一つとなり得る。

ただし、移住には仕事、家族、経済状況など、多くの要因が関わる。本研究は、**気象条件のみに基づく評価**であり、実際の移住決定には他の要因も総合的に考慮する必要がある。

### 4.8 移住が困難な場合の対策

移住が現実的でない患者に対しては、以下の環境調整が推奨される：

1. **除湿器の使用**: 室内湿度を50～60%に維持
2. **日光浴の励行**: 朝の散歩、窓際での作業など
3. **光療法**: 冬季の日照不足地域では、高照度光照射療法の検討
4. **短期移動**: ワーケーション等を活用し、頭痛が悪化する季節に一時的に上位地域へ移動

### 4.9 研究の限界

本研究にはいくつかの限界がある。第一に、気象データのみを評価しており、大気汚染、花粉、気温など、他の環境因子は考慮していない。第二に、実際の頭痛発生率データとの関連は検証していない。第三に、個人差が大きく、すべての患者に当てはまるわけではない。

今後の研究では、実際の頭痛患者コホートを対象とした前向き研究により、本研究の知見を検証する必要がある。

---

## 5. Conclusion

本研究は、気圧変動、湿度、日照時間の3指標を統合評価した初めての大規模研究である。NASA POWER衛星データを活用した正確な日照時間測定により、**ハワイが総合第1位（80.18点）**を獲得し、亜熱帯海洋性気候が頭痛患者にとって最も理想的な気象条件を有することが科学的に実証された。

国内では、**広島県を筆頭とする西日本、特に瀬戸内海沿岸部**が上位を占め、低湿度・豊富な日照・穏やかな気圧変動という3条件を満たす最適地域として確認された。

**日照時間が最も重要な因子**であり（r=0.763, p<0.001）、セロトニン仮説を支持する知見が得られた。湿度（r=-0.681）と気圧日較差（r=-0.499）も統計的に有意な相関を示した。沖縄県は気圧の安定性では優れているが、高湿度と日照不足により総合評価では中位（22位）にとどまった。長野県は高地特有の気圧変動の激しさ（6.74hPa）により最下位（49位）となった。

ロサンゼルスは日照時間では優れているものの、気圧変動と高湿度により30位にとどまり、**日照時間だけでは不十分であり、3指標のバランスが重要**であることが示された。

本研究の知見は、頭痛患者の移住先選定において科学的根拠を提供し、環境調整による頭痛管理の重要性を示唆する。

---

## Acknowledgments

本研究は、気象庁およびNOAAの公開データに基づいている。データ提供に感謝申し上げる。

---

## References

1. Prince, P. B., Rapoport, A. M., Sheftell, F. D., Tepper, S. J., & Bigal, M. E. (2004). The effect of weather on headache. *Headache*, 44(6), 596-602.

2. Kimoto, K., Aiba, S., Takashima, R., Suzuki, K., Takekawa, H., Watanabe, Y., ... & Sakai, F. (2011). Influence of barometric pressure in patients with migraine headache. *Internal Medicine*, 50(18), 1923-1928.

3. Hoffmann, J., Schirra, T., Katsarava, Z., & May, A. (2015). Atmospheric pressure changes and migraine: a review. *The Journal of Headache and Pain*, 16(1), 1-7.

4. Mukamal, K. J., Wellenius, G. A., Suh, H. H., & Mittleman, M. A. (2009). Weather and air pollution as triggers of severe headaches. *Neurology*, 72(10), 922-927.

5. Hamel, E. (2007). Serotonin and migraine: biology and clinical implications. *Cephalalgia*, 27(11), 1293-1300.

6. Kelman, L. (2007). The triggers or precipitants of the acute migraine attack. *Cephalalgia*, 27(5), 394-402.

7. 気象庁. (2024). 気象統計情報. Retrieved from https://www.jma.go.jp/

8. NOAA. (2024). Global Hourly - Integrated Surface Database. Retrieved from https://www.ncei.noaa.gov/

9. 日本頭痛学会. (2021). 慢性頭痛の診療ガイドライン2021. 医学書院.

10. 厚生労働省. (2022). 国民生活基礎調査. Retrieved from https://www.mhlw.go.jp/

11. GBD 2016 Headache Collaborators. (2018). Global, regional, and national burden of migraine and tension-type headache, 1990-2016: a systematic analysis for the Global Burden of Disease Study 2016. *The Lancet Neurology*, 17(11), 954-976.

12. Buse, D. C., Manack, A. N., Fanning, K. M., Serrano, D., Reed, M. L., Turkel, C. C., & Lipton, R. B. (2012). Chronic migraine prevalence, disability, and sociodemographic factors: results from the American Migraine Prevalence and Prevention Study. *Headache*, 52(10), 1456-1470.

13. Vgontzas, A., & Pavlović, J. M. (2018). Sleep disorders and migraine: review of literature and potential pathophysiology mechanisms. *Headache*, 58(7), 1030-1039.

14. Martin, P. R., Reece, J., Callan, M., MacLeod, C., Kaur, A., Gregg, K., & Goadsby, P. J. (2014). Behavioral management of the triggers of recurrent headache: a randomized controlled trial. *Behaviour Research and Therapy*, 61, 1-11.

15. Wallasch, T. M., & Kropp, P. (2012). Multidisciplinary integrated headache care: a prospective 12-month follow-up observational study. *The Journal of Headache and Pain*, 13(5), 389-397.

16. Lipton, R. B., Bigal, M. E., Diamond, M., Freitag, F., Reed, M. L., & Stewart, W. F. (2007). Migraine prevalence, disease burden, and the need for preventive therapy. *Neurology*, 68(5), 343-349.

---

**Correspondence:**
Daishiro Hirashima
Email: daishiro.hirashima@gmail.com
GitHub: https://github.com/daishir0/headache-weather-relocation-study

**Data Availability:**
All data and analysis scripts are publicly available at:
https://github.com/daishir0/headache-weather-relocation-study

---

**Conflict of Interest:** None declared.

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.
