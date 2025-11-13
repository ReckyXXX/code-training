using System;
using System.Threading;
using System.Threading.Tasks;

public class Test
{
    public abstract class BaseState
    {
        protected readonly StateMachine _stateMachine;

        protected BaseState(StateMachine stateMachine)
        {
            _stateMachine = stateMachine;
        }

        public virtual void Enter() 
        {
            Console.WriteLine($"EnterState {GetType()}");
        }
        
        public virtual void Exit() 
        {
            Console.WriteLine($"ExitState {GetType()}");
        }
        
        public virtual void Update() 
        {
            
        }
    }
    
    public class RunState : BaseState
    {
        int _counter = 0;

        public RunState(StateMachine stateMachine) : base(stateMachine)
        {

        }

        public override void Update()
        {
            if (_counter >= 5)
            {
                _stateMachine.ChangeState(new WalkState(_stateMachine));
                return;
            }

            Console.WriteLine("Running");
            _counter++;
        }
    }
    
    public class IdleState : BaseState
    {
        public IdleState(StateMachine stateMachine) : base(stateMachine)
        {

        }
        
        public override void Update()
        {
            Console.WriteLine("Idle");
        }
    }
    
    public class WalkState : BaseState
    {
        public WalkState(StateMachine stateMachine) : base(stateMachine)
        {

        }

        public override void Update()
        {
            Console.WriteLine("Walk");
        }
    }
    
    public class StateMachine 
    {
        BaseState _currentState;
        
        public StateMachine() 
        {
            _currentState = new RunState(this);    
        }
        
        public void Update() 
        {
            _currentState.Update();    
        }
        
        public void ChangeState(BaseState state) 
        {
            _currentState?.Exit();
            _currentState = state;
            _currentState.Enter();
        }
    }
    
	public static void Main()
	{
        Console.WriteLine("Start");
               
        var cts = new CancellationTokenSource();
        var task = Task.Run(() => DoWork(cts.Token));
        
        Console.ReadLine();
        
        cts.Cancel();
        
        task.Wait();
        
        Console.WriteLine("Finish");
	}
	
	static void DoWork(CancellationToken cancellationToken)
    {
        StateMachine stateMachine = new StateMachine();
	    while(!cancellationToken.IsCancellationRequested)
        {
            stateMachine.Update();
            Thread.Sleep(1000);
	    }
	}
}
