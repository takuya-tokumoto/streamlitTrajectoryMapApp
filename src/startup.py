# Description: 地図上に実績データと予測データをプロットする
import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium


# サンプルデータの作成
def create_sample_data() -> pd.DataFrame:
    """サンプルの移動軌跡データを読み込み"""
    return pd.read_csv("dataset\sample_data.csv")


# 地図に移動軌跡をプロットする関数
def plot_trajectory(df: pd.DataFrame, m: folium.Map, radius: float, line_color: str, marker_color: str) -> None:
    """移動軌跡情報を地図上にプロットする

    Args:
        df (pd.DataFrame): 移動軌跡データ
        m (folium.Map): Folium の地図オブジェクト
        radius (float): 円の半径（km）
        line_color (str): 線の色
        marker_color (str): マーカーの色
    """
    # 時間順にデータをソート
    df = df.sort_values(by="time")

    # ポイント間を線でつなぐ
    points = df.apply(lambda r: [r.x, r.y], axis=1).to_list()
    folium.PolyLine(locations=points, color=line_color, weight=2.5, opacity=0.8).add_to(m)

    # 各ポイントにマーカーと円を追加
    for _, row in df.iterrows():
        folium.Marker(
            location=[row.x, row.y],
            popup=f"UID: {row.uid}<br>時間: {row.time}",
            tooltip=f"UID: {row.uid} ({row.time})",
            icon=folium.Icon(color=marker_color),
        ).add_to(m)

        folium.Circle(
            radius=radius * 1000,
            location=[row.x, row.y],
            popup=f"UID: {row.uid}",
            color=marker_color,
            fill=True,
            fill_opacity=0.07,
        ).add_to(m)


# Streamlit アプリのメイン処理
def main():
    st.title("施策対象者の移動軌跡")  # タイトル

    # サンプルデータの読み込み
    trajectory_data = create_sample_data()

    # UID の選択ボックスを作成
    selected_uid = st.selectbox("対象者を選択してください", trajectory_data["uid"].unique())

    # 選択された UID に基づいてデータをフィルタリング
    actual_data = trajectory_data[(trajectory_data["is_pred"] == False) & (trajectory_data["uid"] == selected_uid)]
    predicted_data = trajectory_data[(trajectory_data["is_pred"] == True) & (trajectory_data["uid"] == selected_uid)]

    # 地図の初期設定
    map_center = [actual_data["x"].mean(), actual_data["y"].mean()]
    m = folium.Map(location=map_center, zoom_start=12)

    # 実績データをプロット
    plot_trajectory(actual_data, m, radius=0.25, line_color="blue", marker_color="blue")

    # 予測データをプロット
    plot_trajectory(predicted_data, m, radius=0.25, line_color="red", marker_color="red")

    # 地図情報を表示
    st_folium(m, width=800, height=600)


# アプリの実行
if __name__ == "__main__":
    main()
