from abc import ABC, abstractmethod


class Runner(ABC):
    command: str

    @abstractmethod
    def __init__(self, args: list[str], computer: str) -> None:
        self._args = args
        self._computer = computer
        self._running = False

    @property
    def running(self) -> bool:
        return self._running

    def execute(self) -> None:
        print(f'Running {self.command} on {self._computer} with args {self._args}')
        self._running = True

    def unexecute(self) -> None:
        print(f'Stopped running {self.command} on {self._computer} with args {self._args}')
        self._running = False


class PythonRunner(Runner):
    _command: str = 'python'

    def __init__(self, args: list[str], computer: str) -> None:
        super().__init__(args, computer)


class GoRunner(Runner):
    command: str = 'go'

    def __init__(self, args: list[str], computer: str) -> None:
        super().__init__(args, computer)


class Computer:  # Invoker
    def __init__(self, model: str) -> None:
        self.model = model
        self._queue: list[tuple[Runner, int]] = []
        self._current: dict[int, Runner] = dict()
        self._current_id = 0
        self._log: dict[int, Runner] = dict()

    def add(self, new_command: str) -> None:
        command = new_command.split()
        for runner in PythonRunner, GoRunner:
            if command[0] == runner.command:
                self._current_id += 1
                self._queue.append((runner(command[1:], self.model), self._current_id))
                print(f'New command with runner {runner.__name__} was added to queue of {self.model}')
                break
        else:
            print(f'No runner for command <{new_command}> found')

    def run_next(self) -> None:
        runner, id_ = self._queue.pop(0)
        self._current[id_] = runner
        runner.execute()

    def stop(self, id_: int) -> None:
        runner = self._current.pop(id_, None)
        if runner is None:
            print(f'Runner with id {id_} was not found in current runners')
        else:
            runner.unexecute()
            self._log[id_] = runner

    def revoke(self, id_: int) -> None:
        runner = self._log.pop(id_, None)
        if runner is None:
            print(f'Runner with id {id_} was not found in log of runners')
        else:
            runner.execute()
            self._current[id_] = runner
