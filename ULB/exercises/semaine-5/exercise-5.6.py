def transcription_arn(brin_codant: str) -> str:
    arn = ""
    for i in range(len(brin_codant)):
        if brin_codant[i] == "T":
            arn += "U"
        else:
            arn += brin_codant[i]
    return arn
