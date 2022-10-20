def solution(participant, completion):
    sorted_participant, sorted_completion = sorted(participant), sorted(completion)

    for i in range(len(sorted_participant)):
        completion_pop = sorted_completion.pop()
        participant_pop = sorted_participant.pop()
        if completion_pop != participant_pop:
            return participant_pop

    return sorted_participant.pop()


if __name__ == '__main__':
    print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
