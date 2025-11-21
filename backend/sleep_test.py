import requests as req

url:str = "http://127.0.0.1:5125/"

# try:
# 	for i in range(1, 13):
# 		request:req.Response = req.post(
# 			url=url + "sleep_log",
# 			timeout=2,
# 			json = {
# 				'sleep_start' : i,
# 				'sleep_end' : i+1
# 			}
# 		)
# 	print("TEST_01_GOOD")
# except Exception as e:
# 	print(e)
# print("\n\n")

request:req.Response = req.get(
	url=url + "sleep_log_head",
	timeout=2
)
print(request.json())

rows = request.json()

message:str = f"you slept at {rows[0][1]:02} on last sleep entry"
message += f"\nyou slept at {rows[1][1]:02} on second to the last sleep entry"

if (rows[0][1] > 0 and rows[0][1] <12) or (rows[1][1] > 0 and rows[1][1] <12) :
	message += "\nyou didnt sleep early in both days, no sleep late tonight"
	pass
else:
	message += "\nyou slept early the past 2 days so you get to play league late :DDD"

print(message)
print("\n\n")

request:req.Response = req.get(
	url=url + "sleep_log",
	timeout=2
)

ret_val: str = "\n".join(", ".join(map(str, row)) for row in request.json()) 
print(ret_val)
print("\n\n")

