from django.urls import path, include
from .views import DepositMoneyView,  WithdrawMoneyView, LoanRequestView, LoanListView, PayLoanView, TransactionReportView, TransferView


urlpatterns = [
    path('deposit/', DepositMoneyView.as_view(), name="deposit_money"),
    path('report/', TransactionReportView.as_view(), name="transaction_report"),
    path('withdraw/', WithdrawMoneyView.as_view(), name="withdraw_money"),
    path('loan_request/', LoanRequestView.as_view(), name="loan_request"),
    path('loans/', LoanListView.as_view(), name="loan_list"),
     
     
   path('transfer/', TransferView.as_view(), name='transfer'),
     
    path('loan/<int:loan_id>/', PayLoanView.as_view(), name="loan_pay"),
 
]