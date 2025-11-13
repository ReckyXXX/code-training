// Найти петлю в односвязном списке

public class Test
{
    public class Node
    {
        public Node next;
    }

    static Node CreateList()
    {
        Node root = new Node();
        Node n = root;
        for (int i = 0; i < 5; i++)
        {
            n.next = new Node();
            n = n.next;
        }
        return root;
    }

    static Node CreateLoopedList()
    {
        Node root = new Node();
        Node n = root;
        for (int i = 0; i < 5; i++)
        {
            n.next = new Node();
            n = n.next;
        }
        n.next = root;
        return root;
    }

    static bool CheckListLooped(Node root)
    {
        Node n = root;
        while(n != null)
        {
            Node r = n.next;
            while(r != null)
            {
                if (r == n)
                {
                    return true;
                }
                r = r.next;   
            }
            n = n.next;
        }
        return false;
    }

    public static void Main()
    {
        Node nonLoopedList = CreateList();

        Console.WriteLine($"List1 is {CheckListLooped(nonLoopedList)}");

        Node loopedList = CreateLoopedList();

        Console.WriteLine($"List2 is {CheckListLooped(loopedList)}");
    }
}