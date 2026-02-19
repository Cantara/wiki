# Synchronization

[http://en.wikipedia.org/wiki/Master_Data_Management](http://en.wikipedia.org/wiki/Master_Data_Management)
[http://msdn2.microsoft.com/en-us/library/bb190163.aspx#mdm04_topic4](http://msdn2.microsoft.com/en-us/library/bb190163.aspx#mdm04_topic4)
[http://www.microsoft.com/sharepoint/mdm/default.mspx](http://www.microsoft.com/sharepoint/mdm/default.mspx)
[http://www.dmreview.com/specialreports/2008_77/10001011-1.html?portal=master_data_management](http://www.dmreview.com/specialreports/2008_77/10001011-1.html?portal=master_data_management)
[http://www.dmreview.com/specialreports/2008_69/10001037-1.html?portal=master_data_management](http://www.dmreview.com/specialreports/2008_69/10001037-1.html?portal=master_data_management)

### General MDM Scenarios ( Rippet )

- Single-copy
- Multiple copies, single maintenance---In this approach, master data is added or changed in the single master copy of the data, but changes are sent out to the source systems in which copies are stored locally. Each application can update the parts of the data that are not part of the master data, but they cannot change or add master data. For example, the inventory system might be able to change quantities and locations of parts, but new parts cannot be added, and the attributes that are included in the product master cannot be changed. This reduces the number of application changes that will be required, but the applications will minimally have to disable functions that add or update master data. Users will have to learn new applications to add or modify master data, and some of the things they normally do will not work anymore.
- Continuous merge---In this approach, applications are allowed to change their copy of the master data. Changes made to the source data are sent to the master, where they are merged into the master list. The changes to the master are then sent to the source systems and applied to the local copies. This approach requires few changes to the source systems; if necessary, the change propagation can be handled in the database, so no application code is changed. On the surface, this seems like the ideal solution. Application changes are minimized, and no retraining is required. Everybody keeps doing what they are doing, but with higher-quality, more complete data. This approach does have several issues:
    - Update conflicts are possible and difficult to reconcile. What happens if two of the source systems change a customer's address to different values? There's no way for the MDM system to decide which one to keep, so intervention by the data steward is required; in the meantime, the customer has two different addresses. This must be addressed by creating data-governance rules and standard operating procedures, to ensure that update conflicts are reduced or eliminated.
    - Additions must be remerged. When a customer is added, there is a chance that another system has already added the customer. To deal with this situation, all data additions must go through the matching process again to prevent new duplicates in the master.
    - Maintaining consistent values is more difficult. If the weight of a product is converted from pounds to kilograms and then back to pounds, rounding can change the original weight. This can be disconcerting to a user who enters a value and then sees it change a few seconds later

### Synchronization

- Out of bounds updates - Maps to continous merge
    - EuroSOX? Traceability?
        - Central coordinator ( Service ) provides great advantage
    - Security / Confidensiality
    - Notifications / Polling
        - Need to have a way of writing changes to every subsystem
            - Central coordinator (the service)
            - Distributed coordinator
- Out of bounds additions - Aktuelt?
    - Must handle addition in non-master subsystems

- Avaliability
    - Node goes down
        - Handle batch updates of state
        - Update system when accesed
    - Central coordinator goes down
        - How should systems notify changes? Issue?

### Strategies

Rules engine.

### When should we synchronize?

- Get (!)
- Find (?)
- Update (!)
- Create (!)
### 

![http://www.dmreview.com/media/assets/article/1059676/Agosta_Fig1.gif](http://www.dmreview.com/media/assets/article/1059676/Agosta_Fig1.gif)
![http://www.dmreview.com/media/assets/article/1059676/Agost_Fig2.gif](http://www.dmreview.com/media/assets/article/1059676/Agost_Fig2.gif)

[http://www.dmreview.com/news/1059676-1.html](http://www.dmreview.com/news/1059676-1.html)
