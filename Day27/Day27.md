# Build a draggable and resizable dashboard with Streamlit Elements

## 参考サイト

https://qiita.com/ak-sakatoku/items/4b5e8bffab3cc5199d02#day-27

https://knowledge.insight-lab.co.jp/aidx/30daysofstreamlit-day27-streamlit-elements-%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%97%E3%81%A6%E3%83%89%E3%83%A9%E3%83%83%E3%82%B0%E5%8F%AF%E8%83%BD%E3%81%A7%E3%82%B5%E3%82%A4%E3%82%BA%E5%A4%89%E6%9B%B4%E5%8F%AF%E8%83%BD%E3%81%AA%E3%83%80%E3%83%83%E3%82%B7%E3%83%A5%E3%83%9C%E3%83%BC%E3%83%89%E3%82%92%E6%A7%8B%E7%AF%89%E3%81%99%E3%82%8B

## コメント

```text
# This is where we will draw our Bump chart.
#
# For this exercise, we can just adapt Nivo's example and make it work with Streamlit Elements.
# Nivo's example is available in the 'code' tab there: https://nivo.rocks/bump/
#
# Data takes a dictionary as parameter, so we need to convert our JSON data from a string to
# a Python dictionary first, with `json.loads()`.
#
# For more information regarding other available Nivo charts:
# https://nivo.rocks/
```

```text
ここでバンプチャートを描画します。

この演習では、Nivo の例を改変して Streamlit Elements で動作するようにできます。
Nivo の例は、https://nivo.rocks/bump/ の「コード」タブで入手できます。

データは辞書をパラメーターとして受け取るため、まず `json.loads()` を使用して JSON データを文字列から Python 辞書に変換する必要があります。

利用可能なその他の Nivo チャートの詳細については、以下をご覧ください。
https://nivo.rocks/
```

## で、結局なにやればいい？

1. https://nivo.rocks/bump/ にアクセス
2. 右側のbump chartの上にある data をクリック
3. 表示されるJSONデータをコピーして`data.json`として保存
