# training-course-2024-2p
script to preprocess and analyze two-photon imaging data

## installation 

### 1. データを適当なフォルダに移す
例えば"C:\Users\User\Desktop"
### 2. anaconda のインストール https://docs.anaconda.com/anaconda/install/
### 3. suite2pのインストール https://github.com/MouseLand/suite2p
 
> Open an anaconda prompt / command prompt with conda for python 3 in the path <br>
Create a new environment with conda create --name suite2p python=3.9. <br>
To activate this new environment, run conda activate suite2p <br>
~~(Option 1) You can install the minimal version of suite2p, run python -m pip install suite2p.~~ <br>
(Option 2) You can install the GUI version with python -m pip install suite2p[gui]. If you're on a zsh server, you may need to use ' ' around the suite2p[gui] call: python -m pip install 'suite2p[gui]'. This also installs the NWB dependencies. <br>
Now run python -m suite2p and you're all set. <br>
Running the command suite2p --version in the terminal will print the install version of suite2p.
"
>
GUIが起動したら、2光子データのtiffファイルの入ったフォルダーを移し、RUN

### 4. 　解析用レポジトリのインストール　https://github.com/NeuralDynamics-Tamagawa/training-course-2024-2p/
anaconda promptを開き適当なフォルダに移動(e.g. cd C:\Users\User\Desktop)
`git clone https://github.com/NeuralDynamics-Tamagawa/training-course-2024-2p/` <br>

### 5. vscodeで上記フォルダーを開く
Select KernelでPython Environmentを選択 -> Create python environment
terminalでpip install requirements.txt

### 6. main.ipynbを実行




