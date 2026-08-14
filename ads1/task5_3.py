"""Tests for task 5."""

import unittest
import random
from task5 import Queue
from task5_2 import queue_rotate, queue_reverse, StackQueue, CycleQueue


class Task5MainTests(unittest.TestCase):
    """Class for unit tests for the main task."""

    def test_enqueue(self) -> None:
        """Tests how enquue() adds elements."""
        queue: Queue = Queue()
        for i in range(10):
            queue.enqueue(i)

        self.assertEqual(10, queue.size(),
            "Queue size is incorrect after enqueuing.")

        expected: list[int] = list(range(10))

        result: list[int] = []
        for i in range(queue.size()):
            result.append(queue.dequeue())

        self.assertEqual(expected, result,
            "Enqueue-dequeue pair is inconsistent.")

    def test_enqueue_null(self) -> None:
        """Tests how enqueue() adds elements to an empty queue."""
        queue: Queue = Queue()

        self.assertEqual(0, queue.size(),
            "Size is not zero in an empty queue.")

        queue.enqueue(6)

        self.assertEqual(1, queue.size(),
            "Size of a one-element long queue is not 1.")
        self.assertEqual(6, queue.dequeue(),
            "Queue-dequeue pair is inconsistent in a one-element long queue.")

    def test_dequeue(self) -> None:
        """Tests how dequeue() removes elements."""
        queue: Queue = Queue()
        for i in range(10):
            queue.enqueue(i)

        for i in range(queue.size()):
            queue.dequeue()

        self.assertEqual(0, queue.size(),
            "Queue size after dequeuing is incorrect.")

    def test_dequeue_null(self) -> None:
        """Tests how dequeue() works on an empty queue."""
        queue: Queue = Queue()

        self.assertIsNone(queue.dequeue(),
            "Dequeue() on an empty queue doesn't return None.")
        self.assertEqual(0, queue.size(),
            "Queue size is incorrect after dequeue() on an empty queue.")

    def test_queue_large(self) -> None:
        """Tests how enqueue() and dequeue() work on a large queue."""
        # Run 1000 times
        for i in range(1000):
            queue: Queue = Queue()
            sequence: list[int] = random.choices(range(1, 1000), k=1000)
            for j in range(len(sequence)):
                queue.enqueue(sequence[j])

            self.assertEqual(len(sequence), queue.size(),
                "Size of a large queue is incorrect after enqueuing.")

            result: list[int] = []
            for j in range(queue.size()):
                result.append(queue.dequeue())

            self.assertEqual(0, queue.size(),
                "Size of a large queue is incorrect after enqueue-dequeue.")
            self.assertEqual(sequence, result,
                "Enqueue-dequeue pair is inconsistent in a large queue.")


class Task5ExtraTests(unittest.TestCase):
    """Class for unit tests for the extra task."""

    # Tests for the queue rotation (ex 3.*)
    def test_rotation(self) -> None:
        """Tests rotation function on a common case."""
        queue: Queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        queue_rotate(queue, 3)

        expected: list[int] = []
        for i in range(10):
            expected.append((i + 3) % 10)

        result: list[int] = []
        for i in range(queue.size()):
            result.append(queue.dequeue())

        self.assertEqual(expected, result,
            "Rotation is incorrect.")

    def test_rotation_null(self) -> None:
        """Tests rotation function on an empty queue."""
        queue: Queue = Queue()

        queue_rotate(queue, 3)

        self.assertEqual(0, queue.size(),
            "Queue rotation changed size of an empty queue.")

    def test_rotation_large(self) -> None:
        """Tests rotation function on a large queue."""
        # Run 1000 times
        for i in range(1000):
            queue: Queue = Queue()
            for j in range(1000):
                queue.enqueue(j)
            steps: int = random.randint(0, 1000)
            queue_rotate(queue, steps)

            expected: list[int] = []
            for j in range(1000):
                expected.append((j + steps) % 1000)

            result: list[int] = []
            for j in range(queue.size()):
                result.append(queue.dequeue())

            self.assertEqual(expected, result,
                "Rotation of a large queue is incorrect.")

    # Tests for the stack-based queue implementation (ex 4.*)
    def test_stack_enqueue(self) -> None:
        """Tests how enquue() adds elements (stack-based)."""
        queue: StackQueue = StackQueue()
        for i in range(10):
            queue.enqueue(i)

        self.assertEqual(10, queue.size(),
            "Queue size is incorrect after enqueuing.")

        expected: list[int] = list(range(10))

        result: list[int] = []
        for i in range(queue.size()):
            result.append(queue.dequeue())

        self.assertEqual(expected, result,
            "Enqueue-dequeue pair is inconsistent.")

    def test_stack_enqueue_null(self) -> None:
        """Tests how enqueue() adds elements to an empty queue (stack-based)"""
        queue: StackQueue = StackQueue()

        self.assertEqual(0, queue.size(),
            "Size is not zero in an empty queue.")

        queue.enqueue(6)

        self.assertEqual(1, queue.size(),
            "Size of a one-element long queue is not 1.")
        self.assertEqual(6, queue.dequeue(),
            "Queue-dequeue pair is inconsistent in a one-element long queue.")

    def test_stack_dequeue(self) -> None:
        """Tests how dequeue() removes elements (stack-based)."""
        queue: StackQueue = StackQueue()
        for i in range(10):
            queue.enqueue(i)

        for i in range(queue.size()):
            queue.dequeue()

        self.assertEqual(0, queue.size(),
            "Queue size after dequeuing is incorrect.")

    def test_stack_dequeue_null(self) -> None:
        """Tests how dequeue() works on an empty queue (stack-based)."""
        queue: StackQueue = StackQueue()

        self.assertIsNone(queue.dequeue(),
            "Dequeue() on an empty queue doesn't return None.")
        self.assertEqual(0, queue.size(),
            "Queue size is incorrect after dequeue() on an empty queue.")

    def test_stack_queue_large(self) -> None:
        """Tests how enqueue() and dequeue() work on a large queue (stack)."""
        # Run 1000 times
        for i in range(1000):
            queue: StackQueue = StackQueue()
            sequence: list[int] = random.choices(range(1, 1000), k=1000)
            for j in range(len(sequence)):
                queue.enqueue(sequence[j])

            self.assertEqual(len(sequence), queue.size(),
                "Size of a large queue is incorrect after enqueuing.")

            result: list[int] = []
            for j in range(queue.size()):
                result.append(queue.dequeue())

            self.assertEqual(0, queue.size(),
                "Size of a large queue is incorrect after enqueue-dequeue.")
            self.assertEqual(sequence, result,
                "Enqueue-dequeue pair is inconsistent in a large queue.")

    # Tests for the queue reversal (ex 5.*)
    def test_reversal(self) -> None:
        """Tests queue reversal on a common case."""
        queue: Queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        queue_reverse(queue)

        expected: list[int] = []
        for i in range(10):
            expected.append(9 - i)

        result: list[int] = []
        for i in range(queue.size()):
            result.append(queue.dequeue())

        self.assertEqual(expected, result,
            "Reversal is incorrect.")

    def test_reversal_null(self) -> None:
        """Tests queue reversal on an empty queue."""
        queue: Queue = Queue()

        queue_reverse(queue)

        self.assertEqual(0, queue.size(),
            "Queue reversal changed size of an empty queue.")

    def test_reversal_large(self) -> None:
        """Tests queue reversal on a large queue."""
        # Run 1000 times
        for i in range(1000):
            queue: Queue = Queue()
            for j in range(1000):
                queue.enqueue(j)
            queue_reverse(queue)

            expected: list[int] = []
            for j in range(1000):
                expected.append(999 - j)

            result: list[int] = []
            for j in range(queue.size()):
                result.append(queue.dequeue())

            self.assertEqual(expected, result,
                "Reversal of a large queue is incorrect.")

    # Tests for the cyclic queue implementation (ex 6.*)
    def test_cyclic_enqueue(self) -> None:
        """Tests how enquue() adds elements (cyclic)."""
        queue: CycleQueue = CycleQueue(10)
        for i in range(10):
            queue.enqueue(i)

        self.assertEqual(10, queue.size(),
            "Queue size is incorrect after enqueuing.")

        expected: list[int] = list(range(10))

        result: list[int] = []
        for i in range(queue.size()):
            result.append(queue.dequeue())

        self.assertEqual(expected, result,
            "Enqueue-dequeue pair is inconsistent.")

    def test_cyclic_enqueue_null(self) -> None:
        """Tests how enqueue() adds elements to an empty queue (cyclic)."""
        queue: CycleQueue = CycleQueue(1)

        self.assertEqual(0, queue.size(),
            "Size is not zero in an empty queue.")

        queue.enqueue(6)

        self.assertEqual(1, queue.size(),
            "Size of a one-element long queue is not 1.")
        self.assertEqual(6, queue.dequeue(),
            "Queue-dequeue pair is inconsistent in a one-element long queue.")

    def test_cyclic_enqueue_full(self) -> None:
        """Test how enqueue() works on a filled-up queue."""
        queue: CycleQueue = CycleQueue(10)
        for i in range(100):
            queue.enqueue(i)

        self.assertEqual(10, queue.size(),
            "Queue size isn't at the max capacity limit.")

        expected: list[int] = list(range(10))

        result: list[int] = []
        for i in range(queue.size()):
            result.append(queue.dequeue())

        self.assertEqual(expected, result,
            "Enqueue-dequeue pair in a full queue is inconsistent.")

    def test_cyclic_dequeue(self) -> None:
        """Tests how dequeue() removes elements (cyclic)."""
        queue: CycleQueue = CycleQueue(10)
        for i in range(10):
            queue.enqueue(i)

        for i in range(queue.size()):
            queue.dequeue()

        self.assertEqual(0, queue.size(),
            "Queue size after dequeuing is incorrect.")

    def test_cyclic_dequeue_null(self) -> None:
        """Tests how dequeue() works on an empty queue (cyclic)."""
        queue: CycleQueue = CycleQueue(0)

        self.assertIsNone(queue.dequeue(),
            "Dequeue() on an empty queue doesn't return None.")
        self.assertEqual(0, queue.size(),
            "Queue size is incorrect after dequeue() on an empty queue.")

    def test_cyclic_queue_large(self) -> None:
        """Tests how enqueue() and dequeue() work on a large queue (cyclic)."""
        # Run 1000 times
        for i in range(1000):
            queue: CycleQueue = CycleQueue(750)
            sequence: list[int] = random.choices(range(1, 1000), k=750)
            for j in range(len(sequence)):
                queue.enqueue(sequence[j])
            # Make the internal head index rotate
            for j in range(queue.size()):
                queue.dequeue()
            for j in range(len(sequence)):
                queue.enqueue(sequence[j])

            self.assertEqual(len(sequence), queue.size(),
                "Size of a large queue is incorrect after enqueuing.")

            result: list[int] = []
            for j in range(queue.size()):
                result.append(queue.dequeue())

            self.assertEqual(0, queue.size(),
                "Size of a large queue is incorrect after enqueue-dequeue.")
            self.assertEqual(sequence, result,
                "Enqueue-dequeue pair is inconsistent in a large queue.")


if __name__ == '__main__':
    unittest.main()



