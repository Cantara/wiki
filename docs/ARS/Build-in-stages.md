# Build in stages

One way of reducing release length is to build a limited version of a feature and later make it more comprehensive. This often works best when combined with a [limited release](limited-release.md). This principle is best explained with examples:

### Outsourced print
In Google Docs the print function simply creates a PDF document and then opens a PDF<sub>~viewer. The user then prints by using the print function in the PDF</sub>~viewer. By "outsourcing" the problem of printing Google Docs avoided having to support all the intricacies of printing in an early release. The penalty for the user is relatively minor, an extra click on Print in the PDF-viewer.

### Simple security
In a distributed application there is often a need to be able to communicate in a secure way. Implementing secure communication can be complex and time consuming. The first release can avoid this by simply depending on leased VPN lines. This strategy will often require a [limited release](limited-release.md) in order to not incur unacceptable leasing costs.

### Read only integration
When building a new system that will access an existing system a first release can be limited to only providing the possibility of viewing information, not modifying it. The risks involved in releasing a system that can not alter information is much lower than with a system that has editing features.
