# Author				: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date					: ur my date uwu
# Description			: Code that will impress u ;)
# Actual Description	: Creating a database to log my sleep schedules
# ========================================================================
# HEADERS
# ========================================================================

import sqlite3
import textwrap
from datetime import datetime, timezone

from db_connection import SQLConnection

# ========================================================================
# FUNCTIONS 
# ========================================================================

class DBSleep(SQLConnection):

	DB_FILE:str = r"sleep_log.db"

	# ========================================================================

	def INIT_table_sleep_log(self)->None:
		CREATE_table_sleep_log = """
		CREATE TABLE IF NOT EXISTS sleep_log (
			time_stamp TEXT,
			
			hour_sleep_start INT,
			hour_sleep_end INT,

			id INTEGER PRIMARY KEY AUTOINCREMENT
		);
		"""
		self.SQL_execute(SQL_command=CREATE_table_sleep_log)

	# ========================================================================

	def CREATE_sleep_log(
			self,
			hour_sleep_start:int = -1, 
			hour_sleep_end:int = -1
		) -> None:

		self.INIT_table_sleep_log()
		time_now:str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

		INSERT_sleep_log = f"""
		INSERT INTO sleep_log (
			time_stamp, hour_sleep_start, hour_sleep_end
		) VALUES (
			{self.SQL_value(time_now)},
			{self.SQL_value(hour_sleep_start)},
			{self.SQL_value(hour_sleep_end)}
		);
		"""
		self.SQL_execute(INSERT_sleep_log)

	def GET_sleep_log(self)->list:
		SQL_command = """
		SELECT * FROM sleep_log
		ORDER BY id DESC
		LIMIT 20;
		"""

		rows:list = self.SQL_fetch(SQL_command)
		return rows

	# ========================================================================

	def GET_sleep_log_last_2(self)->list:
		SQL_command = """
		SELECT * FROM sleep_log
		ORDER BY id DESC
		LIMIT 2;
		"""
		rows:list = self.SQL_fetch(SQL_command)

		return rows
