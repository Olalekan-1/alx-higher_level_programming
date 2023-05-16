#include "lists.h"

/**
 * is_palindrome - To check if a linked list is palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome else 0
 */

int is_palindrome(listint_t **head)
{	listint_t *slow, *fast, *p1, *p2, *secondHalf, *midNode, *prevSlow;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = *head;
	fast = *head;
	prevSlow = *head;
	midNode = NULL;
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prevSlow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		midNode = slow;
		slow = slow->next;
	}
	secondHalf = reverse_listint(&slow);
	prevSlow->next = NULL;
	p1 = *head;
	p2 = secondHalf;
	while (p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			return (0);
		}
		p1 = p1->next;
		p2 = p2->next;
	}
	secondHalf = reverse_listint(&secondHalf);
	if (midNode != NULL)
	{
		prevSlow->next = midNode;
		midNode->next = secondHalf;
	}
	else
	prevSlow->next = secondHalf;
	return (1);
}





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


