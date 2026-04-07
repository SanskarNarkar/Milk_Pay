from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
import datetime
from .models import User, MilkEntry, RateConfig
from .forms import FarmerSignUpForm, MilkEntryForm, RateForm

@login_required
def dashboard(request):
    if request.user.is_superuser or request.user.is_admin:
        return redirect('admin_dashboard')
    elif request.user.is_farmer:
        return redirect('farmer_dashboard')
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    # 1. Handle Forms
    if request.method == 'POST' and 'add_milk' in request.POST:
        form = MilkEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        milk_form = MilkEntryForm()

    current_rate = RateConfig.objects.last()
    if request.method == 'POST' and 'update_rate' in request.POST:
        r_form = RateForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            return redirect('admin_dashboard')

    # 2. Filter Logic (Month/Year/Farmer)
    today = timezone.now().date()
    selected_month = int(request.GET.get('month', today.month))
    selected_year = int(request.GET.get('year', today.year))
    farmer_id = request.GET.get('farmer_id')

    # Base Filter: Month & Year
    entries = MilkEntry.objects.filter(date__month=selected_month, date__year=selected_year)

    selected_farmer = None
    farmer_stats = None

    if farmer_id:
        selected_farmer = get_object_or_404(User, id=farmer_id, is_farmer=True)
        entries = entries.filter(farmer=selected_farmer)
        
        # Calculate totals for this view
        total_liters = entries.aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_pay = entries.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        farmer_stats = {'liters': total_liters, 'pay': total_pay}
    
    entries = entries.order_by('-date', '-created_at')
    farmers = User.objects.filter(is_farmer=True)
    


    # Generate Month List for Dropdown
    month_list = []
    curr = today
    for i in range(12):
        month_list.append((curr.month, curr.year, curr.strftime('%B %Y')))
        # Go back one month
        first = curr.replace(day=1)
        curr = first - datetime.timedelta(days=1)

    context = {
        'milk_form': milk_form,
        'rate_form': RateForm(instance=current_rate),
        'current_rate': current_rate,
        'entries': entries,
        'farmers': farmers,
        'selected_farmer': selected_farmer, 
        'farmer_stats': farmer_stats,
        'selected_month': selected_month,
        'selected_year': selected_year,
        'month_list': month_list
    }
    return render(request, 'core/admin_dashboard.html', context)

@login_required
def farmer_dashboard(request):
    today = timezone.now().date()
    
    # Current Month (Buffer)
    current_entries = MilkEntry.objects.filter(
        farmer=request.user, 
        date__month=today.month, 
        date__year=today.year
    ).order_by('-date')

    current_pay = current_entries.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
    current_liters = current_entries.aggregate(Sum('quantity'))['quantity__sum'] or 0

    # Full History
    all_entries = MilkEntry.objects.filter(farmer=request.user).order_by('-date')

    context = {
        'current_entries': current_entries,
        'current_pay': current_pay,
        'current_liters': current_liters,
        'all_entries': all_entries 
    }
    return render(request, 'core/farmer_dashboard.html', context)

# --- Standard Action Views (Keep these) ---
@login_required
def edit_entry(request, entry_id):
    if not request.user.is_superuser:
        return redirect('dashboard') 
    entry = get_object_or_404(MilkEntry, id=entry_id)
    if request.method == 'POST':
        form = MilkEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = MilkEntryForm(instance=entry)
    return render(request, 'core/edit_entry.html', {'form': form, 'entry': entry})


#register farmer 
@login_required
def register_farmer(request):
    if request.method == 'POST':
        form = FarmerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FarmerSignUpForm()
    return render(request, 'core/register_farmer.html', {'form': form})

@login_required
def delete_farmer(request, user_id):
    if request.user.is_superuser:
        farmer = get_object_or_404(User, id=user_id)
        farmer.delete()
    return redirect('admin_dashboard')

# Import the new form first!
from .forms import FarmerSignUpForm, MilkEntryForm, RateForm, FarmerUpdateForm

#farmer edit view
@login_required
def edit_farmer(request, user_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    
    farmer = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = FarmerUpdateForm(request.POST, instance=farmer)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = FarmerUpdateForm(instance=farmer)
    
    return render(request, 'core/edit_farmer.html', {'form': form, 'farmer': farmer})