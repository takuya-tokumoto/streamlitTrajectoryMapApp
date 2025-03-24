
# 施策対象者の移動軌跡可視化アプリ

地図上に「実績（Actual）」と「予測（Predicted）」の移動軌跡を同時にプロットする Streamlit アプリです。  
Folium を使ったインタラクティブな地図上で、対象者（UID）ごとの行動パターンを簡単に比較・分析できます。

---

## 📝 Features

- UID（ユーザID）選択による対象者フィルタリング  
- 実績データは青線・青マーカー、予測データは赤線・赤マーカーで表示  
- マーカークリックで日時・UID のポップアップ表示  
- 円形オーバーレイで半径（km）による影響範囲を可視化  
- Streamlit UI なのでノーコードで起動・共有可能  

---

## 🚀 Getting Started

### Installation

```bash
git clone https://github.com/takuya-tokumoto/streamlitTrajectoryMap.git
cd streamlitTrajectoryMap
```

```bash
conda create -n {環境名} python=3.10
conda activate {環境名}
pip install -r requirements.txt

```

---

## 📂 Directory Structure

```
streamlitTrajectoryMap/
├── app.py                  # Streamlit エントリポイント
├── requirements.txt        # Python ライブラリ一覧
├── README.md               # 本ドキュメント
└── data/                   # （オプション）CSV 等の実データ格納フォルダ
```

---

## 🎯 Usage

```bash
streamlit run src/startup.py
```

1. ブラウザが自動で開きます（http://localhost:8501）  
2. サイドバーから対象者（UID）を選択  
3. 地図上に「実績（青）」と「予測（赤）」の軌跡が表示  

---

## 🔧 Customization

| Parameter     | 説明                           | デフォルト |
|---------------|--------------------------------|------------|
| `radius`      | マーカー周囲の円の半径（km）    | 0.25       |
| `line_color`  | 軌跡ラインの色                 | blue/red   |
| `marker_color`| マーカーの色                   | blue/red   |

`plot_trajectory()` 関数の引数を変更することで調整可能です。

---

## 📊 Data Format

| Column | 型      | 説明                              |
|--------|---------|-----------------------------------|
| uid    | str     | ユーザID                          |
| x      | float   | 緯度                              |
| y      | float   | 経度                              |
| time   | ISO8601 | 日時 (`YYYY-MM-DDTHH:MM:SS`)       |
| is_pred| bool    | 予測データか否か                  |

- サンプルデータは `create_sample_data()` 内に定義済み
