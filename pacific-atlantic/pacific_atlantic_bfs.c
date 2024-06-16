#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct Point - Represents a point in a 2D grid.
 * @row: The row index of the point.
 * @col: The column index of the point.
 */
typedef struct Point
{
	int row;
	int col;
} Point;

/**
 * struct Queue - Represents a queue of Points.
 * @points: A dynamic array of Points.
 * @size: The current number of Points in the queue.
 * @capacity: The current capacity of the queue.
 * @front: The index of the front element.
 * @rear: The index of the rear element.
 */
typedef struct Queue
{
	Point *points;
	int size;
	int capacity;
	int front;
	int rear;
} Queue;

/**
 * createQueue - Creates a new Queue with a given capacity.
 * @capacity: The initial capacity of the new Queue.
 * Return: A pointer to the new Queue.
 */
Queue *createQueue(int capacity)
{
	Queue *q;

	q = (Queue *)malloc(sizeof(Queue));
	if (q == NULL)
		return (NULL);

	q->points = (Point *)malloc(sizeof(Point) * capacity);
	if (q->points == NULL)
	{
		free(q);
		return (NULL);
	}

	q->size = 0;
	q->capacity = capacity;
	q->front = 0;
	q->rear = -1;
	return (q);
}

/**
 * enqueue - Adds a new Point to the end of a Queue.
 * @q: The Queue to add the Point to.
 * @row: The row index of the new Point.
 * @col: The column index of the new Point.
 */
void enqueue(Queue *q, int row, int col)
{
	if (q->size == q->capacity)
	{
		q->capacity *= 2;
		q->points = (Point *)realloc(q->points, sizeof(Point) * q->capacity);
		if (q->points == NULL)
			return;
	}

	q->rear = (q->rear + 1) % q->capacity;
	q->points[q->rear].row = row;
	q->points[q->rear].col = col;
	q->size++;
}

/**
 * dequeue - Removes and returns the first Point in a Queue.
 * @q: The Queue to remove the Point from.
 * Return: The first Point in the Queue.
 */
Point dequeue(Queue *q)
{
	Point front;

	front = q->points[q->front];
	q->front = (q->front + 1) % q->capacity;
	q->size--;
	return (front);
}

/**
 * isEmpty - Checks if a Queue is empty.
 * @q: The Queue to check.
 * Return: true if the Queue is empty, false otherwise.
 */
bool isEmpty(Queue *q)
{
	return (q->size == 0);
}

/**
 * freeQueue - Frees the memory allocated for a Queue.
 * @q: The Queue to free.
 */
void freeQueue(Queue *q)
{
	free(q->points);
	free(q);
}

/**
 * bfs - Performs a breadth-first search on a 2D grid.
 * @heights: The 2D grid to search.
 * @heightsSize: The number of rows in the grid.
 * @heightsColSize: An array containing the number of columns in each row.
 * @visited: A 2D boolean array to keep track of which cells have been visited.
 * @q: A Queue used for the breadth-first search.
 */
void bfs(int **heights, int heightsSize, int *heightsColSize, bool **visited,
		Queue *q)
{
	int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
	int i, nr, nc;
	Point p;

	while (!isEmpty(q))
	{
		p = dequeue(q);
		for (i = 0; i < 4; i++)
		{
			nr = p.row + directions[i][0];
			nc = p.col + directions[i][1];
			if (nr >= 0 && nr < heightsSize && nc >= 0 && nc < heightsColSize[nr] &&
					!visited[nr][nc] && heights[nr][nc] >= heights[p.row][p.col])
			{
				visited[nr][nc] = true;
				enqueue(q, nr, nc);
			}
		}
	}
}

/**
 * pacificAtlantic - Finds all cells that can flow to both the
 * Pacific and Atlantic oceans.
 * @heights: The 2D grid to search.
 * @heightsSize: The number of rows in the grid.
 * @heightsColSize: An array containing the number of columns in each row.
 * @returnSize: Pointer to the number of resulting arrays.
 * @returnColumnSizes: Pointer to the array of sizes of the resulting arrays.
 *
 * Description: This function uses a breadth-first search (BFS) to identify
 * all cells in the given heights grid that can flow water to both the
 * Pacific and Atlantic oceans. The Pacific Ocean touches the top and left
 * edges of the grid, while the Atlantic Ocean touches the bottom and right
 * edges. Water can flow from a cell to its adjacent cells if the height of
 * the adjacent cell is less than or equal to the height of the current cell.
 *
 * Return: A 2D array of coordinates.
 */
int **pacificAtlantic(int **heights, int heightsSize, int *heightsColSize,
		int *returnSize, int **returnColumnSizes)
{
	int ROWS, COLS, r, c, **result, i;
	bool **pacificVisited, **atlanticVisited;
	Queue *pacificQueue, *atlanticQueue;

	ROWS = heightsSize;
	COLS = heightsColSize[0];

	/* Allocate memory for visited arrays */
	pacificVisited = (bool **)malloc(ROWS * sizeof(bool *));
	atlanticVisited = (bool **)malloc(ROWS * sizeof(bool *));
	if (pacificVisited == NULL || atlanticVisited == NULL)
		return (NULL);

	for (r = 0; r < ROWS; r++)
	{
		pacificVisited[r] = (bool *)malloc(COLS * sizeof(bool));
		atlanticVisited[r] = (bool *)malloc(COLS * sizeof(bool));
		if (pacificVisited[r] == NULL || atlanticVisited[r] == NULL)
			return (NULL);

		memset(pacificVisited[r], 0, COLS * sizeof(bool));
		memset(atlanticVisited[r], 0, COLS * sizeof(bool));
	}

	/* Create queues for BFS */
	pacificQueue = createQueue(ROWS + COLS);
	atlanticQueue = createQueue(ROWS + COLS);
	if (pacificQueue == NULL || atlanticQueue == NULL)
		return (NULL);

	/* Initialize the BFS queues with border cells */
	for (r = 0; r < ROWS; r++)
	{
		pacificVisited[r][0] = true;
		atlanticVisited[r][COLS - 1] = true;
		enqueue(pacificQueue, r, 0);
		enqueue(atlanticQueue, r, COLS - 1);
	}

	for (c = 0; c < COLS; c++)
	{
		pacificVisited[0][c] = true;
		atlanticVisited[ROWS - 1][c] = true;
		enqueue(pacificQueue, 0, c);
		enqueue(atlanticQueue, ROWS - 1, c);
	}

	/* Perform BFS for both oceans */
	bfs(heights, ROWS, heightsColSize, pacificVisited, pacificQueue);
	bfs(heights, ROWS, heightsColSize, atlanticVisited, atlanticQueue);

	/* Collect the result cells */
	result = (int **)malloc(ROWS * COLS * sizeof(int *));
	*returnColumnSizes = (int *)malloc(ROWS * COLS * sizeof(int));
	*returnSize = 0;
	if (result == NULL || *returnColumnSizes == NULL)
		return (NULL);

	for (r = 0; r < ROWS; r++)
	{
		for (c = 0; c < COLS; c++)
		{
			if (pacificVisited[r][c] && atlanticVisited[r][c])
			{
				result[*returnSize] = (int *)malloc(2 * sizeof(int));
				if (result[*returnSize] == NULL)
					return (NULL);

				result[*returnSize][0] = r;
				result[*returnSize][1] = c;
				(*returnColumnSizes)[*returnSize] = 2;
				(*returnSize)++;
			}
		}
	}

	/* Free allocated memory */
	for (i = 0; i < ROWS; i++)
	{
		free(pacificVisited[i]);
		free(atlanticVisited[i]);
	}
	free(pacificVisited);
	free(atlanticVisited);
	freeQueue(pacificQueue);
	freeQueue(atlanticQueue);

	return (result);
}

/**
 * main - Entry point of the program.
 *
 * Description: This function sets up a 2D grid of heights and calls the
 * pacificAtlantic function to find all cells that can flow to both the
 * Pacific and Atlantic oceans. The results are then printed to the console.
 *
 * Return: 0 if the program completes successfully, or an error code otherwise.
 */
int main(void)
{
	int heightsSize = 5;
	int heightsColSize[5] = {5, 5, 5, 5, 5};
	int *heights[5];
	int i;
	int row0[] = {1, 2, 2, 3, 5};
	int row1[] = {3, 2, 3, 4, 4};
	int row2[] = {2, 4, 5, 3, 1};
	int row3[] = {6, 7, 1, 4, 5};
	int row4[] = {5, 1, 1, 2, 4};
	int returnSize;
	int *returnColumnSizes;
	int **result;

	/* Initialize the heights array */
	heights[0] = row0;
	heights[1] = row1;
	heights[2] = row2;
	heights[3] = row3;
	heights[4] = row4;

	 /* Initialize returnSize and returnColumnSizes */
	returnSize = 0;
	returnColumnSizes = NULL;

	result = pacificAtlantic(
			heights, heightsSize, heightsColSize,
			&returnSize, &returnColumnSizes
			);

	printf("Result:\n");
	for (i = 0; i < returnSize; i++)
	{
		printf("[%d, %d]\n", result[i][0], result[i][1]);
		free(result[i]);
	}
	free(result);
	free(returnColumnSizes);

	return (0);
}
