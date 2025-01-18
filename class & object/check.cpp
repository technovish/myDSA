#include<stdio.h>
#include<conio.h>
#include<alloc.h>

struct stud
{
	int rno;
	char nm[10];
	struct stud *next;
}*start;

void insert_first();
void insert_last();
void insert_at_spec_loc();
void delet_first();
void delet_last();
void delet_node_no();
void search();
void sort();
void display();
void update();
void main()
{
	int choice;

	do
	{
	clrscr();
	printf("\t\t   Menu");
	printf("\n===========================================================");
	printf("\n\t1.Insert First");
	printf("\n\t2.Insert Last");
	printf("\n\t3.Insert at Specific Location");
	printf("\n\t4.Delete First");
	printf("\n\t5.Delete Last");
	printf("\n\t6.Delete Specific Location");
	printf("\n\t7.Search");
	printf("\n\t8.Sort");
	printf("\n\t9.Display");
	printf("\n\t10.Update");
	printf("\n\t0.Exit");

	printf("\n\nEnter Your Choice:");
	scanf("%d",&choice);

	switch(choice)
	{
		case 1:
			insert_first();
			break;
		case 2:
			insert_last();
			break;
		case 3:
			insert_at_spec_loc();
			break;
		case 4:
			delet_first();
			break;
		case 5:
			delet_last();
			break;
		case 6:
			delet_node_no();
			break;
		case 7:
			search();
			break;
		case 8:
			sort();
			break;
		case 9:
			display();
			break;
		case 10:
			update();
			break;
		case 0:
			printf("Bye..Bye");
			break;

	}
	getch();
}while(choice!=0);
getch();
}

void insert_first()
{
	struct stud *newnode;
	newnode=(struct stud *)malloc(sizeof(struct stud));
	printf("\nEnter Roll no.:");
	scanf("%d",&newnode->rno);
	printf("Enter Name:");
	fflush(stdin);
	gets(newnode->nm);
	newnode->next=start;
	start=newnode;


}
void insert_last()
{
	struct stud *node;
	if(start==NULL)
	{
		node=(struct stud *)malloc(sizeof(struct stud));
		node->next=start;
		start=node;
	}
	else
	{
		node=start;
		while(node->next!=NULL)
		{
			node=node->next;
		}
		node->next=(struct stud *)malloc(sizeof(struct stud));
		node=node->next;
		node->next=NULL;
	}
	printf("Enter Roll no.:");
	scanf("%d",node->rno);
	printf("Enter Name:");
	fflush(stdin);
	gets(node->nm);
}
void insert_at_spec_loc()
{
	struct stud *node,*tmp;
	int count=0,i=1,no;
	node=start;

	while(node!=NULL)
	{
		count++;
		node=node->next;
	}
	printf("Enter Node Position:");
	scanf("%d",&no);

	if(no==1)
	{
		insert_first();
	}
       else if(no==count+1)
	{
		insert_last();
	}
	else
	{
		node=start;
		while(i<no-1)
		{
			i++;
			node=node->next;
		}
		tmp->next=node->next;
		node->next=tmp;
		tmp=(struct stud *)malloc(sizeof(struct stud));
		printf("Enter Roll no.:");
		scanf("%d",&tmp->rno);
		printf("Enter Name:");
		fflush(stdin);
		gets(tmp->nm);
	}
  }
void delet_first()
{
	struct stud *node;
	if(start==NULL)
	{
		printf("Empty");
	}
	else
	{

		node=start;
		printf("\n\nInfo deleted");
		printf("\nRoll no.:%d",node->rno);
		printf("\nName:%s",node->nm);

		start=node->next;
	}



}
void delet_last()
{
	struct stud *node,*tmp;
	if(start==NULL)
	{
		printf("Empty");
	}
	else
	{

		node=start;
		while(node->next->next!=NULL)
		{
			node=node->next;
		}
		tmp=node->next;
		node->next=NULL;
	}
		printf("Deleted Info");
		printf("\nRoll no:%d",tmp->rno);
		printf("\nName:%s",tmp->nm);

}
void delet_node_no()
{
	struct stud *node,*tmp;
	int count,no,i=1;

	if(start==NULL)
	{
		printf("Empty");
	}
	else
	{
		node=start;
		while(node!=NULL)
		{
			count++;
			node=node->next;
		}
		printf("Enter Node no.to Delete:");
		scanf("%d",&no);

		if(no==1)
		{
			delet_first();
		}
		else if(no==count)
		{
			delet_last();
		}
		else
		{
			node=start;
			while(i<no-1)
			{
				i++;
				node=node->next;
			}
			tmp=node->next;
			node->next=tmp->next;
			printf("\nInfo Deleted");
			printf("\nRoll no.:%d",tmp->rno);
			printf("\nName:%s",tmp->nm);
			free(tmp);
		}
	}
}
void sort()
{
}
void search()
{
	int ser;
	struct stud *node;
	if(start==NULL)
	{
		printf("\nEmpty");
	}
	else
	{
		printf("Enter Roll no. to Search:");
		scanf("%d",&ser);
		node=start;
		while(node!=NULL)
		{
			if(node->rno==ser)
			{
				printf("\nSearch Info");
				printf("\nRoll no.:%d",node->rno);
				printf("\nName:%s",node->nm);
				break;
			}
			node=node->next;
		}
		if(node==NULL)
		{
			printf("Value Not Found");
		}
	}

}
void display()
{
	struct stud *node;
	if(start==NULL)
	{
		printf("\nEmpty");
	}
	else
	{
		node=start;
		while(node!=NULL)
		{
			printf("\n\nRoll no:%d",node->rno);
			printf("\nName:%s",node->nm);
			node=node->next;

		}
	}

}
void update()
{
	int ser;
	struct stud *node;
	if(start==NULL)
	{
		printf("\nLink List is Empty");
	}
	else
	{
		printf("\nEnter Roll no. to updete:");
		scanf("%d",&ser);

		if(node==NULL)
		{
			printf("Value not Found");
		}
		else
		{

			node=start;
			while(node!=NULL)
			{
				if(node->rno==ser)
				{
					printf("\nEnter Roll no.:");
					scanf("%d",&node->rno);
					printf("\nName:");
					fflush(stdin);
					gets(node->nm);
				}
				node=node->next;
			}

		}
	}
}
