# Optical Quantum Teleportation with Strawberry Fields

このプロジェクトは、光量子計算ライブラリ **Strawberry Fields** を使用して、連続変数（CV）量子テレポーテーションをシミュレーションするものです。

Python 3.10.5 環境において、最新の Strawberry Fields (v0.23.0+) の構文に対応した実装を行っています。

## 概要
コヒーレント状態 $|\alpha\rangle$ を、量子もつれ（EPR対）と古典情報のフィードバックを用いて別のモードへ転送します。

### 実装のポイント
- **最新のAPI構造**: `sf.Program` と `sf.Engine` を分離した最新の記述法を採用。
- **ガウシアン・バックエンド**: 高速なガウシアン・シミュレーションを実行。
- **古典フィードバック**: 測定結果（RegRef）を `.par` を介してリアルタイムでゲートパラメータに反映。
- **可視化**: 転送後の状態をウィグナー関数（Wigner function）でプロットし、転送精度を視覚的に確認可能。

## 環境構築
以下の環境で動作確認済みです。
- Python 3.10.5
- Strawberry Fields
- NumPy
- Matplotlib

```bash
pip install strawberryfields numpy matplotlib
