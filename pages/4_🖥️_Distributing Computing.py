import streamlit as st 
from streamlit_option_menu import option_menu


st. set_page_config(layout="wide")

st.title("Distributed Computing")



st.write("###")
# List of video URLs
video_urls = {
    "What is distrbuted Computing":"https://www.youtube.com/watch?v=lySvlsHtBzM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=3&pp=iAQB",
    "Benefits of distrbuted Computing":"https://www.youtube.com/watch?v=1DecxFubdlw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=4&pp=iAQB",
    "Relation with System Components":"https://www.youtube.com/watch?v=32vwQz67JKk&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=5&pp=iAQB",
    "Distributec vs parallal Computing":"https://www.youtube.com/watch?v=-r33V9Pw4iE&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=6&pp=iAQB",
    "Message Passing vs Shared Memory":"https://www.youtube.com/watch?v=FZ2fBkK31Wc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=7&pp=iAQB",
    "Primitives for Distributed Computing - 1":"https://www.youtube.com/watch?v=rdIzsfc7caU&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=8&pp=iAQB",
    "Primitives for Distributed Computing - 2":"https://www.youtube.com/watch?v=xrxuPOPXkkc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=9&pp=iAQB",
    "Synchoronous vs Asynchoronous":"https://www.youtube.com/watch?v=wGr65b5HXKA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=10&pp=iAQB",
    "Design Issues and Challenge - 1":"https://www.youtube.com/watch?v=Ej3OiG2-6B8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=11&pp=iAQB",
    "Design Issues and Challange - 2":"https://www.youtube.com/watch?v=rWMMyY3mq_g&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=12&pp=iAQB",
    "Distributed program":"https://www.youtube.com/watch?v=TvtFacEeU2o&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=13&pp=iAQB",
    "Model of Communication network":"https://www.youtube.com/watch?v=pSew2vnmumA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=14&pp=iAQB",
    "Global State of Distribution System":"https://www.youtube.com/watch?v=0ae_V9BQvEQ&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=15&pp=iAQB",
    "Logical Clock Basics":"https://www.youtube.com/watch?v=Hu208M7T6R4&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=17&pp=iAQB",
    "Physical Clock Synchronization using NTP":"https://www.youtube.com/watch?v=QEHxlxJF7g8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=18&pp=iAQB",
    "Framework for logical clock":"https://www.youtube.com/watch?v=a5MaMWXB_e0&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=19&pp=iAQB",
    "Scalar Time":"https://www.youtube.com/watch?v=BPHgY4iI5ms&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=20&pp=iAQB",
    "Vector Time":"https://www.youtube.com/watch?v=ueWDUxGHF_k&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=21&pp=iAQB",
    "Global State":"https://www.youtube.com/watch?v=T25bnhg5piM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=22&pp=iAQB",
    "System model Definition":"https://www.youtube.com/watch?v=esym6rotTy4&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=23&pp=iAQB",
    "Chandral Lamport Snapshot Algorithm":"https://www.youtube.com/watch?v=l101NMxx2hc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=24&pp=iAQB",
    "Introduction to MUX":"https://www.youtube.com/watch?v=rNBfoQj6RME&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=25&pp=iAQB",
    "Preliminaries of MUX":"https://www.youtube.com/watch?v=zQb-9dR4Hlw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=26&pp=iAQB",
    "Lamport Algorithm of MUX":"https://www.youtube.com/watch?v=IHmixOPOFRM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=27&pp=iAQB",
    "lamport Algorithm Proof":"https://www.youtube.com/watch?v=yJeIe2ZfWG0&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=28&pp=iAQB",
    "Ricart Agarwala Algorithm - 1":"https://www.youtube.com/watch?v=_bTLQC9bHPM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=29&pp=iAQB",
    "Ricart Agarwala Algorithm - 2":"https://www.youtube.com/watch?v=KInZ3ukchks&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=30&pp=iAQB",
    "Susuki Kasami Algorithm - 1":"https://www.youtube.com/watch?v=ezaKOAUBomw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=31&pp=iAQB",
    "Susuki Kasami Algorithm - 2":"https://www.youtube.com/watch?v=hizWxLaQD0E&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=32&pp=iAQB",
    "Deadlock Basic - 1":"https://www.youtube.com/watch?v=xfXfaToNIZE&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=33&pp=iAQB",
    "Deadlock Basic - 2":"https://www.youtube.com/watch?v=G5OvWW_EfXI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=34&pp=iAQB",
    "Models Of Deadlock":"https://www.youtube.com/watch?v=qRlxuLIf7Do&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=35&pp=iAQB",
    "Chandy Misra Haas for AND Model":"https://www.youtube.com/watch?v=KHeUv2wwt3g&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=36&pp=iAQB",
    "Chandy Misra Haas for OR Model":"https://www.youtube.com/watch?v=KHeUv2wwt3g&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=36&pp=iAQB",
    "Introduction to Consensus":"https://www.youtube.com/watch?v=uoy9ZnqB_84&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=38&pp=iAQB",
    "Byzantine agreement and other problem":"https://www.youtube.com/watch?v=_f9tQ0nTWKc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=39&pp=iAQB",
    "Consensus Algorithm for Crash Failure":"https://www.youtube.com/watch?v=alchs2BBrAY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=40&pp=iAQB",
    "Upper Bound on Byzantine process":"https://www.youtube.com/watch?v=aB-sxVShbLQ&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=41&pp=iAQB",
    "Byzantine Tree Recursive Algorithm":"https://www.youtube.com/watch?v=5gY15nZqrmc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=42&pp=iAQB",
    "Byzantine Tree Iterative Algorithm":"https://www.youtube.com/watch?v=nUp7E_gbdYY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=43&pp=iAQB",
    "Phase King Algorithm":"https://www.youtube.com/watch?v=AvSv2-nn_wA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=44&pp=iAQB",
    "Checkpoint Basic":"https://www.youtube.com/watch?v=YMvgYJj7yMM&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=45&pp=iAQB",
    "Checkpoint Background and Definition":"https://www.youtube.com/watch?v=bfafK2t4xG0&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=46&pp=iAQB",
    "Type of Messages":"https://www.youtube.com/watch?v=cKOAa_CUgS8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=47&pp=iAQB",
    "Issues in Failure Recovery":"https://www.youtube.com/watch?v=rvPp90o9Krw&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=48&pp=iAQB",
    "Checkpoint based Recovery - 1":"https://www.youtube.com/watch?v=fWp4AVla2cI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=49&pp=iAQB",
    "Checkpoint based Recovery - 2":"https://www.youtube.com/watch?v=Ft93YGLNg_A&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=51&pp=iAQB",
    "Checkpoint based Recovery - 3":"https://www.youtube.com/watch?v=1M75AYwepjU&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=50&pp=iAQB",
    "Coordinate Checkpoint algorithm":"https://www.youtube.com/watch?v=Anz_52xBhjc&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=52&pp=iAQB",
    "Algorithm for Asynchronus Checkpoint and recovery - 1":"https://www.youtube.com/watch?v=eluy9_a0MT8&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=53&pp=iAQB",
    "Algorithm for Asynchronus Checkpoint and recovery - 2":"https://www.youtube.com/watch?v=-CRAI7yfgXo&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=54&pp=iAQB",
    "Introduction to Cloud Computing":"https://www.youtube.com/watch?v=SvcKxpAV-7A&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=55&pp=iAQB",
    "Characteristic of Cloud Computing":"https://www.youtube.com/watch?v=_qpUcuya5pU&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=56&pp=iAQB",
    "Cloud Deployment model":"https://www.youtube.com/watch?v=kdGgEdMxavY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=57&pp=iAQB",
    "Cloud Service Model":"https://www.youtube.com/watch?v=Uc4B4odVGtY&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=58&pp=iAQB",
    "Message Ordering Paradigms":"https://www.youtube.com/watch?v=bg1ny7g0dQI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=59&pp=iAQB",
    "Synchronous Program Order on Asynchronous System":"https://www.youtube.com/watch?v=RnMyyJQkcJk&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=60&pp=iAQB",
    "Casual Order":"https://www.youtube.com/watch?v=BKtid1yJ4HQ&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=61&pp=iAQB",
    "Total Order":"https://www.youtube.com/watch?v=agh2o3vvZHA&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=62&pp=iAQB",
    "Virtualization and Loading Balance":"https://www.youtube.com/watch?v=yhLI8Mln4EI&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=63&pp=iAQB",
    "Asynchronus Execution with Synchronus Communication":"https://www.youtube.com/watch?v=U89NWcw9jsg&list=PLR4Rlu17MDY6RhDmiXVCCu6qII_reYviB&index=64&pp=iAQB"
    # Add more video URLs as needed
}

links = list(video_urls.keys())


tab1,tab2 = st.tabs(["Video","Notes"])

with tab1:
    c1,c2 = st.columns([7,3])

    title = "Computer Networks"
    # Sidebar to display video list
    with c2:
        selected_video_index = option_menu(title, links,default_index=0)

    with c1:
        st.markdown('### **'+selected_video_index+'**')
        st.video(video_urls[selected_video_index])


    js = '''
    <script>
        var body = window.parent.document.querySelector(".menu");
        console.log(body);
        body.scrollTop = 0;
    </script>
    '''

    st.components.v1.html(js)

with tab2:
    st.markdown("### Two Marks")

    st.markdown("""
1. **Define Distributed Computing:**
   Distributed computing refers to the use of multiple interconnected and geographically dispersed computers that work together to achieve a common goal. In a distributed computing environment, tasks are divided among the connected computers, often referred to as nodes, and these nodes collaborate to solve problems, process data, or provide services.

2. **List the Features of Distributed Systems:**
   - **Concurrency:** Multiple components can execute concurrently.
   - **Scalability:** The system can be easily expanded to accommodate increased load.
   - **Fault Tolerance:** The system continues to operate in the presence of failures.
   - **Transparency:** Users perceive the system as a single, integrated entity.
   - **Interoperability:** Components from different vendors can work together.
   - **Resource Sharing:** Resources such as data, files, and processing power can be shared.
   - **Reliability:** The system is dependable and consistently performs its functions.

3. **Distinguish between Synchronous and Asynchronous Execution:**
   - **Synchronous Execution:** In synchronous execution, tasks are executed one after the other in a predetermined order. Each task must wait for the previous one to complete before it starts.
   - **Asynchronous Execution:** In asynchronous execution, tasks operate independently and may not wait for others to finish. Asynchronous systems often use mechanisms like callbacks or events to signal task completion.

4. **What is Middleware:**
   Middleware is software that acts as an intermediary layer between different applications or components in a distributed system. It facilitates communication, data management, and integration between disparate systems, allowing them to work together seamlessly.

5. **Compare Shared Memory versus Message Passing in Distributed Systems:**
   - **Shared Memory:** In shared memory systems, multiple processes share a common, addressable space in memory. Communication is achieved by reading and writing to this shared space.
   - **Message Passing:** In message passing systems, processes communicate by exchanging messages. Each process has its own memory, and communication is achieved through sending and receiving messages.

6. **Short Notes on FIFO and NON-FIFO Network Communication Models:**
   - **FIFO (First-In-First-Out):** In FIFO communication, messages are delivered in the order they were sent, preserving the order of message transmission.
   - **NON-FIFO:** In NON-FIFO communication, the order of message delivery is not guaranteed to follow the order of transmission. Messages may be delivered out of order.

7. **What is Consistent Cut and Inconsistent Cut:**
   - **Consistent Cut:** A consistent cut in a distributed system is a global state that captures a consistent snapshot of the system at a particular point in time, reflecting a moment where events appear to have occurred simultaneously.
   - **Inconsistent Cut:** An inconsistent cut is a global state that does not represent a consistent snapshot of the system. It may include events that logically cannot occur simultaneously.

8. **Identify the Two Popular Orders for the Delivery of Messages in Group Communication:**
   - **Causal Order:** Messages are delivered in the order that respects their causal relationship.
   - **Total Order:** Messages are delivered in the same order to all processes.

9. **Why Scalar Clock is Not Consistent in Distributed Systems:**
   Scalar clocks are not consistent because they do not account for the causality of events. Two events that are causally related may have the same scalar timestamp, leading to inconsistencies in ordering.

10. **Define Casual Order Execution:**
    Casual order execution refers to the execution of events or processes in a distributed system in a way that respects their causal relationships. Events that are causally related must be executed in the order implied by their causal connection.

11. **Define Total Order:**
    Total order in distributed systems refers to a global ordering of events or messages that is consistent across all processes. Every process sees the same order of events, ensuring a uniform perception of the system state.

12. **What are the Two Phases in Obtaining a Global Snapshot:**
    - **Recording Phase:** Capture local states and messages.
    - **Marking Phase:** Identify the consistent cut by analyzing the recorded information.

13. **Identify the Three Basic Approaches for Implementing Distributed Mutual Exclusion:**
    - **Centralized Approach:** A single server controls access to the shared resource.
    - **Distributed Approach with Coordinator:** Processes elect a coordinator to manage access.
    - **Distributed Approach without Coordinator:** Processes communicate to achieve mutual exclusion.

14. **Outline the WFG (Wait-for-Graph):**
    The wait-for-graph is a directed graph representing the wait-for relationships among processes in a distributed system. Nodes represent processes, and edges represent processes waiting for the release of resources held by other processes.

15. **Define Deadlock in Distributed System:**
    A deadlock in a distributed system occurs when a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process, resulting in a cyclic dependency.

16. **Define Deadlock and Give an Example:**
    Deadlock occurs when processes are unable to proceed because each is waiting for the other to release a resource. Example: Process A holds Resource X and waits for Resource Y, while Process B holds Resource Y and waits for Resource X.

17. **Fundamental Concept Behind Edge Chasing in Distributed Computing:**
    Edge chasing is a technique used to detect and resolve distributed deadlocks. It involves tracing the edges of the wait-for graph to identify the cycles causing the deadlock.

18. **Compare Authenticated and Unauthenticated Messages:**
    - **Authenticated Messages:** Messages include information to verify their authenticity, ensuring that the sender's identity and the integrity of the message can be verified.
    - **Unauthenticated Messages:** Messages lack authentication information, making it challenging to verify the source or integrity of the message.

19. **Enumerate Consistent System State:**
    A consistent system state is one where all processes in a distributed system observe a similar or valid snapshot of the system at a particular point in time.

20. **Define Orphan Message:**
    An orphan message is a message in a distributed system that has lost its association with the corresponding sender or receiver, often due to failures or unexpected events.

21. **Why Rollback Recovery of Distributed System is Complicated:**
    Rollback recovery in a distributed system is complicated because it requires coordinating the recovery process among multiple nodes, dealing with the uncertainty of message delivery, and ensuring consistency across the system.

22. **Characteristics of Cloud:**
    - **On-Demand Self-Service:** Users can provision and manage computing resources as needed.
    - **Broad Network Access:** Services are available over the network and accessible through standard mechanisms.
    - **Resource Pooling:** Computing resources are pooled to serve multiple users.
    - **Rapid Elasticity:** Resources can be rapidly scaled up or down based on demand.
    - **Measured Service:** Usage is monitored, controlled, and billed based on the consumed resources.

23. **Use of Replication in Cloud Computing:**
    Replication in cloud computing involves creating redundant copies of data or services across multiple locations to enhance reliability, fault tolerance, and performance.

24. **Define Elasticity:**
    Elasticity in cloud computing refers to the ability to dynamically scale resources up or down based on demand. It allows for flexibility in adapting to changing workloads.

25. **Advantages of Cloud Storage (Any Four):**
    - **Scalability:** Easily scale storage capacity as needed.
    - **Accessibility:** Data can be accessed from anywhere with an internet connection.
    - **Cost-Efficiency:** Pay only for the storage capacity used.
    - **Data Redundancy:** Cloud storage often includes data replication for enhanced reliability.
""")


st.markdown("### Part - B")
st.markdown("""

#### 1. **Explain in detail about the relation to computer system components and interaction of the software components at each processor with neat sketch.**

The interaction between computer system components, specifically hardware and software, is fundamental to the overall functionality of a computer system. Here, I'll provide a detailed explanation of the relationship and interaction between various software components at each processor, accompanied by a sketch.

**Computer System Components:**

1. **Processor (CPU):**
   - **Hardware Component:** The CPU is the central processing unit and is responsible for executing instructions stored in memory.

2. **Memory:**
   - **Hardware Component:** Memory stores data and instructions that the CPU uses during computation.

3. **Input/Output (I/O) Devices:**
   - **Hardware Component:** These devices allow the computer to interact with the external environment, such as keyboards, mice, displays, and storage devices.

4. **System Bus:**
   - **Hardware Component:** The system bus is a communication pathway that connects the CPU, memory, and I/O devices, facilitating data transfer.

5. **Software Components:**

   - **Operating System (OS):**
     - *Role:* The OS manages and coordinates the use of hardware resources, provides an interface for user interaction, and ensures the execution of application programs.
     - *Interaction:* The OS interacts with the CPU scheduler, memory manager, file system, and device drivers.

   - **CPU Scheduler:**
     - *Role:* The CPU scheduler determines which process gets access to the CPU at a given time.
     - *Interaction:* It interacts with the operating system and selects processes from the ready queue for execution.

   - **Memory Manager:**
     - *Role:* Manages the computer's memory hierarchy, allocating and deallocating memory space for processes.
     - *Interaction:* Communicates with the CPU, allocating memory to processes and handling page faults.

   - **File System:**
     - *Role:* Manages files on storage devices, providing a hierarchical structure for data storage and retrieval.
     - *Interaction:* Interacts with the OS, applications, and I/O subsystem for reading and writing data to storage.

   - **Device Drivers:**
     - *Role:* These software components allow the operating system to communicate with and control hardware devices.
     - *Interaction:* Device drivers interact with the OS kernel and facilitate communication with peripheral devices.

**Interaction of Software Components at Each Processor (with Neat Sketch):**

""")
st.image(use_column_width=True, image="https://www.educative.io/api/page/5174069054406656/image/download/6093799456505856")
st.markdown("""

1. **User Applications:**
   - Users interact with applications that run on the operating system.

2. **Operating System (OS):**
   - The OS acts as an intermediary between user applications and hardware components.
   - It communicates with the CPU scheduler, memory manager, file system, and device drivers.

3. **CPU Scheduler:**
   - Determines which process to execute next and manages the CPU's execution timeline.

4. **Memory Manager:**
   - Allocates and deallocates memory space for processes, manages virtual memory, and handles page faults.

5. **File System:**
   - Manages files and directories on storage devices, facilitating data storage and retrieval.

6. **Device Drivers:**
   - Enable communication between the operating system and various hardware devices.

7. **CPU (Processor):**
   - Executes instructions fetched from memory.
   - Interacts with the memory unit, ALU (Arithmetic Logic Unit), and control unit.

8. **Memory Unit:**
   - Stores data and instructions for the CPU to access during computation.

9. **Arithmetic Logic Unit (ALU):**
   - Performs arithmetic and logical operations as directed by the CPU.

10. **Control Unit:**
    - Manages the execution of instructions, coordinating activities within the CPU.

11. **I/O Devices:**
    - Enable interaction between the computer system and the external environment.

12. **System Bus:**
    - Facilitates communication and data transfer between the CPU, memory, and I/O devices.

This sketch and explanation illustrate the intricate interaction between hardware and software components within a computer system, showcasing how the operating system manages resources and facilitates communication to ensure the system's overall functionality.

""")