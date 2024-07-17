import random
import sys


class Node:
    def __init__(self):
        self.tasks = 0
        self.next = None
        self.generated_tasks = 0
        self.pulled_tasks = 0
        self.pushed_tasks = 0
        self.completed_tasks = 0

    def generateTasks(self):
        self.tasks = random.randint(1, 1001)
        self.generated_tasks += self.tasks

    def work(self):
        worked = min(self.tasks, 10 + random.randint(-5, 6))
        self.tasks -= worked
        self.completed_tasks += worked

    def balance(self):
        delta = int(((self.tasks - self.next.tasks) / 3) // 10 * 10)
        if delta < 0:
            delta += 10

        if delta > 0:
            self.push(delta)
            self.next.pull(delta)
        else:
            self.pull(-delta)
            self.next.push(-delta)

    def done(self):
        return self.tasks <= 0

    def pull(self, n):
        self.tasks += n
        self.pulled_tasks += n

    def push(self, n):
        self.tasks -= n
        self.pushed_tasks += n


class Ring:
    def __init__(self, n):
        self.nodes = [Node() for i in range(n)]
        for i in range(n):
            self.nodes[i].next = self.nodes[(i + 1) % n]
        self.rounds = 0

    def all_done(self):
        for node in self.nodes:
            if not node.done():
                return False
        return True

    def round(self):
        for node in self.nodes:
            node.generateTasks()

        while not self.all_done():
            for node in self.nodes:
                node.work()

            shuffled = list(self.nodes)
            random.shuffle(shuffled)
            for node in shuffled:
                node.balance()

    def run(self, rounds):
        self.rounds = rounds
        for _ in range(rounds):
            self.round()

    def stats(self):
        stats = []
        tot_completed = sum(node.completed_tasks for node in self.nodes)
        tot_generated = sum(node.generated_tasks for node in self.nodes)
        tot_pulled = sum(node.pulled_tasks for node in self.nodes)
        tot_pushed = sum(node.pushed_tasks for node in self.nodes)
        if tot_generated != tot_completed:
            raise ValueError('Total generated != total completed',
                             tot_generated, tot_completed)
        if tot_pulled != tot_pushed:
            raise ValueError('Total pulled != total pushed',
                             tot_pulled, tot_pushed)
        for i, node in enumerate(self.nodes, 1):
            stats.append((f'Node{i}', node.generated_tasks, node.pulled_tasks,
                         node.pushed_tasks, node.completed_tasks, node.completed_tasks / tot_completed * 100))
            if node.completed_tasks != node.generated_tasks + node.pulled_tasks - node.pushed_tasks:
                raise ValueError('Completed tasks != generated tasks + pulled tasks - pushed tasks',
                                 node.completed_tasks, node.generated_tasks, node.pulled_tasks, node.pushed_tasks)
        stats.append(('Total', tot_generated, tot_pulled,
                     tot_pushed, tot_completed, 100))
        return stats

    def print_stats(self):
        print('Nodes:', len(self.nodes))
        print('Rounds:', self.rounds)
        stats = self.stats()
        header = ['',
                  'Number of generated tasks',
                  'Number of pulled tasks',
                  'Number of pushed tasks',
                  'Number of completed tasks',
                  'Percent of total tasks performed']
        stats.insert(0, header)
        for s in stats:
            print(','.join(str(x) for x in s))


def main():
    ring = Ring(int(sys.argv[1]))
    ring.run(int(sys.argv[2]))
    ring.print_stats()


if __name__ == '__main__':
    main()
