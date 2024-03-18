import subprocess
import sys

def main():
    # Inicie o jogo como um subprocesso
    python = sys.executable
    game_process = subprocess.Popen([python, "game.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    # Comunique-se com o jogo
    while True:
        # Receba a saída do jogo
        game_output = game_process.stdout.readline().strip()
        print("Jogo:", game_output)
        
        # Envie uma entrada para o jogo
        ai_input = input("1")  # Aqui você pode implementar a lógica da IA para gerar a entrada
        game_process.stdin.write(ai_input + "\n")
        game_process.stdin.flush()
        
        # Verifique se o jogo terminou
        if game_output == "Fim de jogo":
            break
    
    # Encerre o processo do jogo
    game_process.kill()

if __name__ == "__main__":
    main()
