from client import LiteratureReviewClient

def main():
    client = LiteratureReviewClient()
    res = client.synthesize_papers(query='Transformer attention mechanisms')
    print(f"Result for summary: {res['summary']}")

if __name__ == "__main__":
    main()
