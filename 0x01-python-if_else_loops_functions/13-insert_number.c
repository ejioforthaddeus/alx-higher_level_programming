#include "lists.h"
#include <stddef.h>
/**
* insert_node - Used to insert a node into sorted linkedlist
* @head: the head of the linkedlist
* @number: Integer value of the node
* Return: pointer to the new item or Null if fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *current, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->next == NULL)
	{
		new->next = *head;
		return (new);
	}
	if ((*head)->n >= new->n)
	{
		current = *head;
		new->next = current;
		*head = new;
		return (new);
	}
	prev = current = *head;

	while (current != NULL)
	{
		if (current->n >= new->n)
		{
			new->next = current;
			prev->next = new;
			return (new);
		}
		prev = current;
		current = current->next;
	}
	prev->next = new;
	return (new);
}
