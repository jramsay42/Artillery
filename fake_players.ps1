$num = Read-Host -Prompt 'Enter number of fake clients: '
For ($i = 0; $i -lt $num; $i++) {
    python ./src/PlayerInterface.py
}