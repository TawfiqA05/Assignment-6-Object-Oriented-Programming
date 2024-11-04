class State:
    def __init__(self, date, state, positive, probableCases, negative, pending, totalTestResultsSource, totalTestResults,
                 hospitalizedCurrently, hospitalizedCumulative, inIcuCurrently, inIcuCumulative, onVentilatorCurrently,
                 onVentilatorCumulative, recovered, dataQualityGrade, lastUpdateEt, dateModified, checkTimeEt, death,
                 hospitalized, dateChecked, totalTestsViral, positiveTestsViral, negativeTestsViral, positiveCasesViral,
                 deathConfirmed, deathProbable, totalTestEncountersViral, totalTestsPeopleViral, totalTestsAntibody,
                 positiveTestsAntibody, negativeTestsAntibody, totalTestsPeopleAntibody, positiveTestsPeopleAntibody,
                 negativeTestsPeopleAntibody, totalTestsPeopleAntigen, positiveTestsPeopleAntigen, totalTestsAntigen,
                 positiveTestsAntigen, fips, positiveIncrease, negativeIncrease, total, totalTestResultsIncrease, posNeg,
                 deathIncrease, hospitalizedIncrease, hash, commercialScore, negativeRegularScore, negativeScore,
                 positiveScore, score, grade):
        self.date = date
        self.state = state
        self.positive = positive
        self.probableCases = probableCases
        self.negative = negative
        self.pending = pending
        self.totalTestResultsSource = totalTestResultsSource
        self.totalTestResults = totalTestResults
        self.hospitalizedCurrently = hospitalizedCurrently
        self.hospitalizedCumulative = hospitalizedCumulative
        self.inIcuCurrently = inIcuCurrently
        self.inIcuCumulative = inIcuCumulative
        self.onVentilatorCurrently = onVentilatorCurrently
        self.onVentilatorCumulative = onVentilatorCumulative
        self.recovered = recovered
        self.dataQualityGrade = dataQualityGrade
        self.lastUpdateEt = lastUpdateEt
        self.dateModified = dateModified
        self.checkTimeEt = checkTimeEt
        self.death = death
        self.hospitalized = hospitalized
        self.dateChecked = dateChecked
        self.totalTestsViral = totalTestsViral
        self.positiveTestsViral = positiveTestsViral
        self.negativeTestsViral = negativeTestsViral
        self.positiveCasesViral = positiveCasesViral
        self.deathConfirmed = deathConfirmed
        self.deathProbable = deathProbable
        self.totalTestEncountersViral = totalTestEncountersViral
        self.totalTestsPeopleViral = totalTestsPeopleViral
        self.totalTestsAntibody = totalTestsAntibody
        self.positiveTestsAntibody = positiveTestsAntibody
        self.negativeTestsAntibody = negativeTestsAntibody
        self.totalTestsPeopleAntibody = totalTestsPeopleAntibody
        self.positiveTestsPeopleAntibody = positiveTestsPeopleAntibody
        self.negativeTestsPeopleAntibody = negativeTestsPeopleAntibody
        self.totalTestsPeopleAntigen = totalTestsPeopleAntigen
        self.positiveTestsPeopleAntigen = positiveTestsPeopleAntigen
        self.totalTestsAntigen = totalTestsAntigen
        self.positiveTestsAntigen = positiveTestsAntigen
        self.fips = fips
        self.positiveIncrease = positiveIncrease
        self.negativeIncrease = negativeIncrease
        self.total = total
        self.totalTestResultsIncrease = totalTestResultsIncrease
        self.posNeg = posNeg
        self.deathIncrease = deathIncrease
        self.hospitalizedIncrease = hospitalizedIncrease
        self.hash = hash
        self.commercialScore = commercialScore
        self.negativeRegularScore = negativeRegularScore
        self.negativeScore = negativeScore
        self.positiveScore = positiveScore
        self.score = score
        self.grade = grade

# Read the CSV file and create State objects
file_path = "/Users/tawfiqabulail/Downloads/Information Infrastructure I /covid_data_set.csv"

state_objects = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    headers = lines[0].strip().split(',')
    for line in lines[1:]:
        data = line.strip().split(',')
        state = State(*data)
        state_objects.append(state)

# Example: Print the first state object
print(vars(state_objects[0]))