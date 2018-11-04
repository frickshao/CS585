@echo off
cd C:\Users\quanb\PycharmProjects\tweet_scrapper 

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
	"GlenBeck"
	"MittRomney"
	"senJohnMcCain"
	"BernieSanders"
	"ChesterSee"
		) do (
	py tweet_downloader.py %%i
)
pause
