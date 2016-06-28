import sys

def condense_meeting_times(meetingTimes):
	meetingTimes.sort(key=lambda tup: tup[0])

	finalTimes = []

	cur_start, cur_end = meetingTimes[0]

	i = 1
	while i < len(meetingTimes):
		if meetingTimes[i][0] <= cur_end and meetingTimes[i][1] > cur_end:
			cur_end = meetingTimes[i][1]
		elif meetingTimes[i][0] > cur_end:
			finalTimes.append((cur_start, cur_end))
			cur_start, cur_end = meetingTimes[i]
		i += 1
	finalTimes.append((cur_start, cur_end))

	return finalTimes

if __name__ == "__main__":
	meetingTimes = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
	print(condense_meeting_times(meetingTimes))