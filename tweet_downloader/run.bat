@echo off
REM change to directory where tweeet_downloader.py is
cd ~\tweet_downloader 

for %%i in (
	"AzizAnsari"
	"BarackObama"
	"elizabethforma"
	"FunnyAsianDude"
	"GRRMspeaking"
	"KanyeWest"
	"kumailn"
	"ladygaga"
	"lunar_cosmetics"
	"MichaelJohns"
	"pattonoswalt"
	"realDonaldTrump"
	"SarahPalinUSA"
	"UMassAmherst"
	"JoeBiden"
	"SenatorReid"
	"NancyPelosi"
	"GlennBeck"
	"MittRomney"
	"senJohnMcCain"
	"BernieSanders"
	"ChesterSee"
		) do (
	py tweet_downloader.py %%i
)
pause
