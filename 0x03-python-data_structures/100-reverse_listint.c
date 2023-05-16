#include "lists.h"

/**
 * reverse_listint - Function to reverse the link
 * @head: pointer to the headnode
 * Return: reversed node;
 */

listint_t *reverse_listint(listint_t **head)
{	listint_t *nextnode = NULL;
	listint_t *previousnode = NULL;

	if (*head == NULL)
	{
		return (*head);
	}
	while (*head != NULL)
	{
		nextnode = (*head)->next;
		(*head)->next = previousnode;
		previousnode = *head;
		*head = nextnode;
	}
	*head = previousnode;
	return (*head);
}

