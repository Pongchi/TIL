hours, minutes = map(int, input().split())

AL_minutes = minutes - 45 if minutes >= 45 else 60 + minutes - 45
AL_hours = hours if minutes >= 45 else (hours - 1 if hours > 0 else 23)

print(AL_hours, AL_minutes)
