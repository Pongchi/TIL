#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct {
	char name[32];
	int korean, math, eng;
} Student;

typedef struct Node {
	Student *st;
	struct Node *llink;
	struct Node *rlink;
} Node;

int no = 1;
Node *create_node() {
    Student* st = malloc(sizeof(Student));
    Node* new_node = malloc(sizeof(Node));

    printf("Name: ");
    scanf("%s", st->name);
    printf("Korean: ");
    scanf("%d", &st->korean);
    printf("Math: ");
    scanf("%d", &st->math);
    printf("English: ");
    scanf("%d", &st->eng);

    new_node->st = st;
	new_node->llink = new_node->rlink = NULL;
    return new_node;
}
Node* search(Node* current) {
	char search_name[32];
	no = 1;
	
	printf("Enter the name of student: ");
	scanf("%s", search_name);
	
	while (current != NULL) {
		if (strcmp(current->st->name, search_name) == 0) return current;
		current = current->rlink;
		no++;
	}
	
	printf("No data about %s\n", search_name);
	return NULL;
}
void push_node(Node** head, Node *new_node) {
	if (*head == NULL) *head = new_node;
	else {
		Node* tail = *head;
		while (tail->rlink != NULL) tail = tail->rlink;
		tail->rlink = new_node;
		new_node->llink = tail;
	}
}
void remove_node(Node** head, Node *removed) {
	if (removed != NULL) {
		if (*head == removed) {
			*head = removed->rlink;
			if (*head != NULL) (*head)->llink = NULL;
		}
		else {
			if (removed->rlink != NULL) removed->rlink->llink = removed->llink;
			removed->llink->rlink = removed->rlink;
		}
		printf("The data of %s is deleted.\n", removed->st->name);
		free(removed);
	}
}
void show_average(Node *node) {
	if (node != NULL) {
		int sum = node->st->korean + node->st->math + node->st->eng; 
		float average = sum / 3.0;
		printf("%s's average is %.1f\n", node->st->name, average);
	}
}
void show_student(Node *node) {
	if (node != NULL) {
		printf("[%d] Name: %s\n", no, node->st->name);
		printf("[%d] Korean: %d\n", no, node->st->korean);
		printf("[%d] Math: %d\n", no, node->st->math);
		printf("[%d] English: %d\n", no, node->st->eng);
	}
}
void show_all(Node* current) {
	no = 1;
	while (current != NULL) {
		show_student(current);
		current = current->rlink;
		no++;
	}
}

int main() {
	int select = 0;
	Node* head = NULL;
	
	do {
		printf("1. Insert a student\n");
		printf("2. Delete a student\n");
		printf("3. Calculate average\n");
		printf("4. Print all students\n");
		printf("5. Find\n");
		printf("6. Exit\n");
		scanf("%d", &select);
		
		switch (select) {
			case 1:
				push_node(&head, create_node());
				break;
			case 2:
				remove_node(&head, search(head));
				break;
			
			case 3:
				show_average(search(head));
				break;
				
			case 4:
				show_all(head);
				break;
				
			case 5:
				show_student(search(head));
                break;
		}
	} while (select != 6);
	return 0;
}