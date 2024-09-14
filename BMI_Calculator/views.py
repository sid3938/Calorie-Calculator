from django.shortcuts import render
from .forms import BmiForm

def BMI_home(request):
  state = None
  form = BmiForm()

  if request.method == "POST":
      form = BmiForm(request.POST)

      if form.is_valid():
          weight = form.cleaned_data['weight']
          height = form.cleaned_data['height'] / 100      
          
          bmi = weight / (height ** 2)
          
          form.instance.bmi = round(bmi,2)
          form.save()
          
          print(f'Weight: {weight}, Height: {height*100}, BMI: {bmi:.2f}')


          if bmi < 18.5:
              state=f"Underweight: {bmi:.2f}. Consult a healthcare provider."
          elif 18.5 <= bmi < 25.0:
              state=f"Normal weight: {bmi:.2f}. Keep it up!"
          elif 25.0 <= bmi < 30.0:
              state=f"Overweight: {bmi:.2f}. Consider weight management."
          elif 30.0 <= bmi < 35.0:
              state=f"Moderate obesity: {bmi:.2f}. Seek healthcare advice."
          elif 35.0 <= bmi < 40.0:
              state=f"Severe obesity: {bmi:.2f}. Consult a healthcare provider."
          else:  # bmi >= 40.0
              state=f"Very severe obesity: {bmi:.2f}. Immediate healthcare consultation needed."

          print(state)

      else:
          # Handle form errors
          print("Form is invalid.")
  else:
      form = BmiForm()

  return render(request, 'BMI_home.html', {'form': form,'state':state})
