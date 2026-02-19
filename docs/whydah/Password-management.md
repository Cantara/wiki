# Password management

#### User stories

1. Any user can reset password using *username* or *email* without logging in.
   1. |  | email is currently not unique in UIB? |
2. Admin can reset password for another user. The *uid* is known.
3. User can update password when logged in. The *uid* is known.
4. Application can update password. The *uid* is known.

#### Responsibility

- UIB
  - CRUD on user
  - update password
  - reset password using ChangePasswordToken
  - Disable user

- UAS
  - Send email, sms

#### Implementation notes

1. Any user can reset password using *username* or *email* without logging in.
   1. Authenticated application, no authenticated user.
   2. POST /{applicationtokenid}/reset\_password/{uidOrUsernameOrEmail}
      1. Set temp password and generate ChangePasswordToken, return time limited change password uri
      2. UAS or other clients can choose to forward this URI to user on email.
2. Admin can reset password for another user. The *uid* is known.
   1. Authenticated application, authenticated application superuser.
   2. POST /{applicationtokenid}/reset\_password/{uidOrUsernameOrEmail} (same as the regular reset password)
3. User can update password when logged in. The *uid* is known.
   1. Authenticated application, authenticated user, update self.
   2. PUT /{applicationtokenid}/{userTokenId}/user/{uid} (userTokenId for user)
   3. |  | The only application authorized to perform this action is SSOLoginWebApp. All other applications must only be allowed to initiate Password Reset. |
4. Application can update password. The *uid* is known.
   1. Authenticated application, authenticated application superuser, update another.
   2. PUT /{applicationtokenid}/{userTokenId}/user/{uid} (userTokenId for admin)
   3. |  | Only UserAdminWebApp must be allowed to perform real password change. All other applications must only be allowed to initiate Password Reset (see above) |

###### UIB

- POST /{applicationtokenid}/password/{username}/reset
- POST /{applicationtokenid}/password/{username}/change/{changePasswordToken}
- ~~POST /{applicationtokenid}/reset\_password/{uidOrUsernameOrEmail}~~
- ~~PUT /{applicationtokenid}/{userTokenId}/user/{uid}~~

###### UAS

- Call resetpassword in UIB, send email to user

###### Concrete changes

- UIB
  - PasswordResource - cleanup paths and methods
  - Remove email sending

- UAS
  - Expose UIB endpoints
  - Expose new endpoint which sends email on password reset

- SSO Login Webapp
  - Perform Password change for loged-in user.
  - Perform Password change when user has received password reset link. This link is distributed via email.

---

#### Old Implementation notes

###### UAS

1. POST /{applicationtokenid}/resetpassword/{usernameOrEmail}
   1. SetTempPassword: PUT /{applicationtokenid}/{userTokenId}/user/{uid}
   2. sendResetPasswordEmail with url with special ChangePasswordToken.
      1. The GUI exposed for changing the password is in SSOLoginWebapp, *PasswordChangeController*.
2. PUT /{applicationtokenid}/{userTokenId}/user/{uid} (userTokenId for user)
3. PUT /{applicationtokenid}/{userTokenId}/user/{uid} (userTokenId for admin)

###### UIB

- Password can be updated
  - Use the regular PUT endpoint to update UserIdentity?
    - PUT /{applicationtokenid}/{userTokenId}/user/{uid}
