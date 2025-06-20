# training-course-2025-2p
2光子データの前処理の手順についての説明。

## 概要
2光子の実験で取得されたデータは

channel 1: iGluSnFR3 (green, グルタミン酸インジケーター）

channel 2: jRGECO (red, カルシウムインジケーター）

のフレームを交互に含む.raw形式のファイルで保存されている。

これを適切なchannel情報に分けて.tiff形式で保存し直して、
suite2p(神経科学者が開発したROI抽出用のソフトウェア）でゆれ補正＋ROI抽出を行い、
各ROIの輝度変化情報を数値として扱えるようにする。

## Installation 

### 1. 配布された実験データを適当なフォルダに移す
例えば"C:\Users\User\Desktop"

### 2. VScodeのインストール
https://code.visualstudio.com/download

python及びjupyterの拡張機能もインストールする
左側のExtensionsタブを選択してpythonと入力すると候補に挙がるので、installをクリックする。jupyterも同様

![image](https://github.com/user-attachments/assets/fb222193-d6e0-40bb-995e-3436852aed6f)


### 3. anaconda のインストール 
https://docs.anaconda.com/anaconda/install/

（もしくは配布されたデータのなかにAnaconda3-2024.10-1-Windows-x86_64.exeファイルがあるので、これをダブルクリックして実行する）

### 4. suite2pのインストール 
https://github.com/MouseLand/suite2p
 
> Open an anaconda prompt / command prompt with conda for python 3 in the path <br>
Create a new environment with conda create --name suite2p python=3.9. <br>
To activate this new environment, run conda activate suite2p <br>
~~(Option 1) You can install the minimal version of suite2p, run python -m pip install suite2p.~~ <br>
(Option 2) You can install the GUI version with python -m pip install suite2p[gui]. If you're on a zsh server, you may need to use ' ' around the suite2p[gui] call: python -m pip install 'suite2p[gui]'. This also installs the NWB dependencies. <br>
Now run python -m suite2p and you're all set. <br>
Running the command suite2p --version in the terminal will print the install version of suite2p.
"


### 5. pythonのインストール　（不要かも）
例えばmicrosoft storeからpython 3.13をインストール
https://apps.microsoft.com/detail/9pnrbtzxmb4z?hl=ja-JP&gl=JP


### 6. 　解析用レポジトリのインストール　https://github.com/NeuralDynamics-Tamagawa/training-course-2025-2p/
~~anaconda promptを開き適当なフォルダに移動(e.g. cd C:\Users\User\Desktop)~~
~~git clone https://github.com/NeuralDynamics-Tamagawa/training-course-2024-2p/~~ <br>
ZIPでダウンロードして解凍する


### 7. vscodeで上記フォルダーを開く
Select KernelでPython Environmentを選択 -> Create python environment

### 6. main.ipynbをvscodeで実行
(途中でsuite2p GUI内での操作あり）



