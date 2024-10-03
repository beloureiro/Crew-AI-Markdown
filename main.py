import time
import logging
from tqdm import tqdm  # Para barra de progresso
from crew import MarkdownCrew

# Configuração de logging
logging.basicConfig(
    filename='logs/crew_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define o caminho completo para o arquivo a ser verificado
file_path = r"D:\OneDrive - InMotion - Consulting\AI Projects\Crew-AI-Trraining\Db\report_1.txt"

def execute_crew():
    start_time = time.time()  # Início da execução
    logging.info("Markdown Crew execution started.")

    # Feedback inicial indicando que o arquivo será revisado
    feedback = f"Verifying and updating the file: {file_path}"
    logging.info(f"Feedback provided: {feedback}")

    # Instancia a crew de markdown
    crew_instance = MarkdownCrew()

    # Executa o workflow da crew com o caminho do arquivo
    result = crew_instance.crew().kickoff(inputs={"feedback": feedback, "file_path": file_path})
    logging.info("Markdown Crew workflow executed successfully.")

    # Barra de progresso e log dos resultados das tarefas
    print("\nExecuting tasks with progress:\n")
    for task_output in tqdm(result.tasks_output, desc="Tasks Progress", unit="task"):
        logging.info(f"Task result: {task_output}")

    # Calcula a duração total da execução
    end_time = time.time()
    total_duration = end_time - start_time
    logging.info(f"Total execution time: {total_duration:.2f} seconds")

    print("Execution completed. Check the logs for more details.")

if __name__ == "__main__":
    execute_crew()
