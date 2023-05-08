#include "lists.h"

/**
 * check_cycle - check if list has cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is loop else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
