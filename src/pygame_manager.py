import threading

# Глобальные переменные управления
pygame_window_running = False
pygame_thread = None
stop_event = threading.Event()


def run_with_check(target_func, *args):
    global pygame_window_running, pygame_thread, stop_event

    # Завершаем уже работающий поток, если он есть
    if pygame_window_running and pygame_thread is not None:
        stop_event.set()
        pygame_thread.join()

    # Сброс события и запуск нового окна
    stop_event = threading.Event()
    pygame_thread = threading.Thread(
        target=target_func_wrapper,
        args=(target_func, stop_event, *args),
        daemon=True
    )
    pygame_thread.start()


def target_func_wrapper(target_func, stop_event_local, *args):
    global pygame_window_running
    pygame_window_running = True

    try:
        # Передаём stop_event внутрь модели
        target_func(*args, stop_event_local)
    finally:
        pygame_window_running = False
