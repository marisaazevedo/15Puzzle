import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.function.Predicate;
import java.util.stream.IntStream;

public class FifteenPuzzle {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int[][] start = IntStream.range(0, 4)
                .mapToObj(i -> readLine(scanner))
                .toArray(int[][]::new);

        int[][] solution = {
                {  1,  2,  3,  4 },
                {  5,  6,  7,  8 },
                {  9, 10, 11, 12 },
                { 13, 14, 15,  0 }
        };

        Board board = breadthFirstSearch(start, solution);
        System.out.println(board);
        System.out.println(Arrays.deepToString(board.board()));
    }

    private static int[] readLine(Scanner scanner) {
        return Arrays.stream(scanner.nextLine().split("\\s+"))
                .filter(Predicate.not(String::isEmpty))
                .mapToInt(Integer::parseInt)
                .toArray();
    }

    private static Board breadthFirstSearch(int[][] start, int[][] solution) {
        Queue<Board> queue = new LinkedList<>();
        Set<int[][]> visited = new HashSet<>();

        queue.add(new Board(start));
        while (!queue.isEmpty()) {
            Board board = queue.poll();

            if (Arrays.deepEquals(board.board(), solution)) {
                return board;
            }

            board.moves().stream()
                    .filter(move -> visited.add(move.board()))
                    .forEach(queue::add);
        }

        throw new NoSuchElementException();
    }

}

record Board(int[][] board, int plays, Point blank) {
    private static final int BLANK = 0;

    Board(int[][] board) {
        this(board, 0, findBlank(board));
    }

    List<Board> moves() {
        return Arrays.stream(Direction.values())
                .map(this::move)
                .flatMap(Optional::stream)
                .toList();
    }

    private Optional<Board> move(Direction direction) {
        Point next = this.blank.move(direction);

        if (checkBoundaries(next)) {
            int[][] clone = swap(this.blank, next);
            return Optional.of(new Board(clone, this.plays + 1, next));
        }

        return Optional.empty();
    }

    private int[][] swap(Point source, Point target) {
        int[][] clone = Arrays.stream(this.board).map(int[]::clone).toArray(int[][]::new);

        if (clone[source.y()][source.x()] == BLANK) {
            clone[source.y()][source.x()] = clone[target.y()][target.x()];
            clone[target.y()][target.x()] = BLANK;
        }

        return clone;
    }

    private boolean checkBoundaries(Point point) {
        return 0 <= point.y() && point.y() < this.board.length
                && 0 <= point.x() && point.x() < this.board[point.y()].length;
    }

    private static Point findBlank(int[][] board) {
        for (int y = 0; y < board.length; y++) {
            for (int x = 0; x < board[y].length; x++) {
                if (board[y][x] == BLANK) {
                    return new Point(y, x);
                }
            }
        }
        throw new NoSuchElementException();
    }
}

record Point(int y, int x) {
    Point move(Direction direction) {
        return switch (direction) {
            case UP -> new Point(this.y - 1, this.x);
            case DOWN -> new Point(this.y + 1, this.x);
            case LEFT -> new Point(this.y, this.x - 1);
            case RIGHT -> new Point(this.y, this.x + 1);
        };
    }
}

enum Direction {
    UP, DOWN, LEFT, RIGHT
}
