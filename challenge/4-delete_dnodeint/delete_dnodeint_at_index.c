#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - deletes the node at index of a dlistint_t list
 * @head: double pointer to the head of the list
 * @index: index of the node to delete, starting at 0
 *
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	unsigned int i = 0;

	if (*head == NULL)
		return (-1);

	while (i < index)
	{
		if (*head == NULL)
			return (-1);
		*head = (*head)->next;
		i++;
	}

	if ((*head)->prev == NULL && (*head)->next == NULL)
	{
		free(*head);
		*head = NULL;
		return (1);
	}

	if ((*head)->prev == NULL)
	{
		*head = (*head)->next;
		free((*head)->prev);
		(*head)->prev = NULL;
		return (1);
	}

	(*head)->prev->next = (*head)->next;
	if ((*head)->next != NULL)
		(*head)->next->prev = (*head)->prev;
	free(*head);
	return (1);
}
