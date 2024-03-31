**Scenario Configuration**


|                    **Name**                    |           **Class**           | **Scenario**                                                                                                                                                                                                                                |
| :---------------------------------------------: | :----------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|           Create CEX Contract Request           |  CEXContractRequestModelTests  | This scenario tests the creation of a CEX contract request along with assigning leaders and managers. It also validates the creation of the request with required fields and checks for validation errors in case of invalid inputs.        |
|    Transition State on CEX Contract Request    |  CEXContractRequestModelTests  | This scenario tests the transition of states for a CEX contract request, including creating snapshots, transitioning to different states, and handling errors for invalid transitions.                                                      |
|       Create Monitoring Contract Request       | MonitoringContractRequestTests | This scenario tests the creation of a monitoring contract request along with assigning leaders and managers. It also validates the creation of the request with required fields and checks for validation errors in case of invalid inputs. |
| Transition State on Monitoring Contract Request | MonitoringContractRequestTests | This scenario tests the transition of states for a monitoring contract request, including creating snapshots, transitioning to different states, and handling errors for invalid transitions.                                               |
|                   Create User                   |         UserModelTests         | This scenario tests the creation of a user, including both regular users and superusers. It validates the creation with required fields, uniqueness constraints, and proper error handling.                                                 |

**Test Case Design**

1. **Test Objective:** Create CEX Contract Request


   | **Model**          | **Method**              | **Scenario**                | **Input**            | **Expected output**                                                          |
   | :----------------- | :---------------------- | :-------------------------- | :------------------- | :--------------------------------------------------------------------------- |
   | CEXContractRequest | create_contract_request | Create CEX Contract Request | Various valid inputs | Successful creation of CEX contract request and manager and leader assigment |
   | CEXContractRequest | create_contract_request | Create CEX Contract Request | Invalid inputs       | Validation error raised                                                      |
2. **Test Objective:** Transition State on CEX Contract Request


   | **Model**          | **Method**          | **Scenario**                             | **Input**                | **Expected output**                         |
   | :----------------- | :------------------ | :--------------------------------------- | :----------------------- | :------------------------------------------ |
   | CEXContractRequest | transition_to_state | Transition State on CEX Contract Request | Valid state transition   | Successful transition and snapshot creation |
   | CEXContractRequest | transition_to_state | Transition State on CEX Contract Request | Invalid state transition | Value error raised                          |
3. **Test Objective:** Create Monitoring Contract Request


   | **Model**                 | **Method**              | **Scenario**                       | **Input**            | **Expected output**                                                                 |
   | :------------------------ | :---------------------- | :--------------------------------- | :------------------- | :---------------------------------------------------------------------------------- |
   | MonitoringContractRequest | create_contract_request | Create Monitoring Contract Request | Various valid inputs | Successful creation of monitoring contract request and manager and leader assigment |
   | MonitoringContractRequest | create_contract_request | Create Monitoring Contract Request | Invalid inputs       | Validation error raised                                                             |
4. **Test Objective:** Transition State on Monitoring Contract Request


   | **Model**                 | **Method**          | **Scenario**                                    | **Input**                | **Expected output**                         |
   | :------------------------ | :------------------ | :---------------------------------------------- | :----------------------- | :------------------------------------------ |
   | MonitoringContractRequest | transition_to_state | Transition State on Monitoring Contract Request | Valid state transition   | Successful transition and snapshot creation |
   | MonitoringContractRequest | transition_to_state | Transition State on Monitoring Contract Request | Invalid state transition | Value error raised                          |
5. **Test Objective:** Create User


   | **Model** | **Method**       | **Scenario** | **Input**              | **Expected output**              |
   | :-------- | :--------------- | :----------- | :--------------------- | :------------------------------- |
   | User      | create_user      | Create User  | Valid user data        | Successful creation of user      |
   | User      | create_user      | Create User  | Duplicate user ID      | Integrity error raised           |
   | User      | create_user      | Create User  | Invalid inputs         | Validation error raised          |
   | User      | create_superuser | Create User  | Valid superuser data   | Successful creation of superuser |
   | User      | create_superuser | Create User  | Duplicate superuser ID | Integrity error raised           |
   | User      | create_superuser | Create User  | Invalid inputs         | Validation error raised          |
