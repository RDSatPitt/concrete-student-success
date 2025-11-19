import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _(
    age,
    athlete,
    credits,
    distance,
    efc,
    epr,
    extracurricular,
    firstgen,
    gender,
    gpa,
    housing,
    legacy,
    merit,
    midterms,
    origins,
    pell,
    pell_plus,
    printer,
    pronouns,
    race,
    residency,
    sai,
    scores,
    transfer,
    unmet,
    wi_fi,
):
    # #constants_1


    variables_by_task = {
        1: {
            "variables": [pell, efc, sai, unmet, merit, pell_plus],
            "header": "Regulatory Gate",
        },
        2: {
            "variables": [race, gender, age, pronouns],
            "header": "Protected-Attribute Gate",
        },
        3: {
            "variables": [gpa, scores, midterms, epr, printer],
            "header": "Data-Reliability Gate",
        },
        4: {
            "variables": [legacy, athlete, firstgen, distance, credits, housing, residency, origins, transfer, extracurricular, wi_fi],
            "header": "Equity & Actionability Gate",
        },
    }

    
    # #     1: {
    # #         "variables": ["pell", "efc", "sai", "unmet", "merit", "pell_plus"],
    # #         "header": ""
    # #     },
    # #     2: {
    # #         "variables": ["race", "gender", "age", "pronouns"],
    # #         "header": "",
    # #     },
    # #     3: {
    # #         "variables": ["gpa", "scores", "midterms", "epr", "printer"],
    # #         "header": "",
    # #     },
    # #     4: {
    # #         "variables": ['legacy', 
    # #                       'athlete', 
    # #                       'firstgen', 
    # #                       'distance', 
    # #                       'credits', 
    # #                       'housing', 
    # #                       'residency', 
    # #                       'origins', 
    # #                       'transfer', 
    # #                       'extracurricular', 
    # #                       'wi_fi'
    # #                      ],
    # #         "header": "",
    # #     }
    # # }
    return (variables_by_task,)


@app.cell
def _():
    textbox_text_boilerplate = 'Please briefly justify your reasoning for your'
    correct = "Right Choice"

    variable_selection_button_labels = {
        1: {
            'include': "Include",
            'exclude': "Exclude",
            'other': "Flag for Review",
        }, 
        2: {
            'include': 'Include As-Is', 
            'exclude': 'Exclude Entirely', 
            'other': 'Keep for Bias-Audit Only'
        },
        3: {
            'include': 'Include as-is', 
            'exclude': 'Exclude (too unreliable)', 
            'other': 'Flag for Data-Quality Improvement'
        },
        4: {
            'include': 'Include as-is', 
            'exclude': 'Exclude (too unreliable)', 
            'other': 'Flag for Data-Quality Improvement'
        }
    }
    return correct, textbox_text_boilerplate, variable_selection_button_labels


@app.cell
def _(
    mo,
    set_age_final,
    set_age_initial,
    set_age_state,
    set_athlete_final,
    set_athlete_initial,
    set_athlete_state,
    set_credits_final,
    set_credits_initial,
    set_credits_state,
    set_distance_final,
    set_distance_initial,
    set_distance_state,
    set_efc_final,
    set_efc_initial,
    set_efc_state,
    set_epr_final,
    set_epr_initial,
    set_epr_state,
    set_extracurricular_final,
    set_extracurricular_initial,
    set_extracurricular_state,
    set_firstgen_final,
    set_firstgen_initial,
    set_firstgen_state,
    set_gender_final,
    set_gender_initial,
    set_gender_state,
    set_gpa_final,
    set_gpa_initial,
    set_gpa_state,
    set_housing_final,
    set_housing_initial,
    set_housing_state,
    set_legacy_final,
    set_legacy_initial,
    set_legacy_state,
    set_merit_final,
    set_merit_initial,
    set_merit_state,
    set_midterms_final,
    set_midterms_initial,
    set_midterms_state,
    set_origins_final,
    set_origins_initial,
    set_origins_state,
    set_pell_final,
    set_pell_initial,
    set_pell_plus_final,
    set_pell_plus_initial,
    set_pell_plus_state,
    set_pell_state,
    set_printer_final,
    set_printer_initial,
    set_printer_state,
    set_pronoun_final,
    set_pronoun_initial,
    set_pronoun_state,
    set_race_final,
    set_race_initial,
    set_race_state,
    set_residency_final,
    set_residency_initial,
    set_residency_state,
    set_sai_final,
    set_sai_initial,
    set_sai_state,
    set_scores_final,
    set_scores_initial,
    set_scores_state,
    set_transfer_final,
    set_transfer_initial,
    set_transfer_state,
    set_unmet_final,
    set_unmet_initial,
    set_unmet_state,
    set_wi_fi_final,
    set_wi_fi_initial,
    set_wi_fi_state,
    textbox_text_boilerplate,
    variable_details,
    variable_selection_button_labels,
):
    def handler(obj, value): 
        setter = obj.state
        initial_feedback = obj.initial_feedback_setter
        final_feedback = obj.final_feedback_setter
        setter(value)
        initial_feedback(retrieve_variable_details(obj, *['feedback', 'initial', value]))
        final_feedback(retrieve_variable_details(obj, *['feedback', 'final', value]))
        # setter = setters[obj]['set_state']
        # initial_feedback = setters[obj]['set_initial']
        # final_feedback = setters[obj]['set_final']
        # initial_feedback_text = retrieve_variable_details(obj, *['feedback', 'initial', value])
        # initial_feedback(initial_feedback_text)
        # final_feedback_text = retrieve_variable_details(obj, *['feedback', 'final', value])
        # final_feedback(final_feedback_text)


    def retrieve_variable_details(obj, *args): 
        sought_item = variable_details[obj.name]
        for item in args: 
            sought_item = sought_item[item]
        return sought_item


    class Variable:
        def __init__(self, name:str, task:int, state_setter, initial_feedback_setter, final_feedback_setter):
            self.name = name
            self.task = task
            self.title = retrieve_variable_details(self, 'title')
            self.definition = retrieve_variable_details(self, 'def')
            self.state = state_setter
            self.initial_feedback_setter = initial_feedback_setter
            self.final_feedback_setter = final_feedback_setter
            self.incl = mo.ui.run_button(label=variable_selection_button_labels[self.task]['include'], 
                                         kind='success', 
                                         on_change=lambda _: handler(self, 'include')
                                        )
            self.excl = mo.ui.run_button(label=variable_selection_button_labels[self.task]['exclude'], 
                                         kind='danger', 
                                         on_change=lambda _: handler(self, 'exclude')
                                        )
            self.flag = mo.ui.run_button(label=variable_selection_button_labels[self.task]['other'], 
                                         kind='warn', 
                                         on_change=lambda _: handler(self, 'other')
                                        )
            self.text = mo.ui.text_area(label=f"{textbox_text_boilerplate} {self.title} choice.", rows=4)
            self.initial_feedback = None
            self.final_feedback = None

        def get_initial_feedback(self, dict): 
            return dict[self]['initial']
    
        def getter(self): 
            return dict[self]['state']


    pell = Variable('pell', 1, set_pell_state, set_pell_initial, set_pell_final)
    efc = Variable('efc', 1, set_efc_state, set_efc_initial, set_efc_final)
    sai = Variable('sai', 1, set_sai_state, set_sai_initial, set_sai_final)
    unmet = Variable('unmet', 1, set_unmet_state, set_unmet_initial, set_unmet_final)
    merit = Variable('merit', 1, set_merit_state, set_merit_initial, set_merit_final)
    pell_plus = Variable('pell_plus', 1, set_pell_plus_state, set_pell_plus_initial, set_pell_plus_final)
    race = Variable("race", 2, set_race_state, set_race_initial, set_race_final)
    gender = Variable("gender", 2, set_gender_state, set_gender_initial, set_gender_final) 
    age = Variable("age", 2, set_age_state, set_age_initial, set_age_final)
    pronouns = Variable("pronouns", 2, set_pronoun_state, set_pronoun_initial, set_pronoun_final)
    gpa = Variable("gpa", 3, set_gpa_state, set_gpa_initial, set_gpa_final)
    scores = Variable("scores", 3, set_scores_state, set_scores_initial, set_scores_final)
    midterms = Variable("midterms", 3, set_midterms_state, set_midterms_initial, set_midterms_final)
    epr = Variable("epr", 3, set_epr_state, set_epr_initial, set_epr_final)
    printer = Variable("printer", 3, set_printer_state, set_printer_initial, set_printer_final)
    legacy=Variable('legacy', 4, set_legacy_state, set_legacy_initial, set_legacy_final)
    athlete=Variable('athlete', 4, set_athlete_state, set_athlete_initial, set_athlete_final)
    firstgen = Variable('firstgen', 4, set_firstgen_state, set_firstgen_initial, set_firstgen_final)
    distance = Variable('distance', 4, set_distance_state, set_distance_initial, set_distance_final) 
    credits=Variable('credits', 4, set_credits_state, set_credits_initial, set_credits_final)
    housing=Variable('housing', 4, set_housing_state, set_housing_initial, set_housing_final)
    residency=Variable('residency', 4, set_residency_state, set_residency_initial, set_residency_final) 
    origins=Variable('origins', 4, set_origins_state, set_origins_initial, set_origins_final)
    transfer=Variable('transfer', 4, set_transfer_state, set_transfer_initial, set_transfer_final) 
    extracurricular=Variable('extracurricular', 4, set_extracurricular_state, set_extracurricular_initial, set_extracurricular_final)
    wi_fi=Variable('wi_fi', 4, set_wi_fi_state, set_wi_fi_initial, set_wi_fi_final)


    # setters = {
    #     pell: {'set_state': set_pell_state, 
    #            'set_initial': set_pell_initial,
    #            'set_final': set_pell_final,
    #           },
    #     efc: {'set_state': set_efc_state, 
    #           'set_initial': set_efc_initial,
    #           'set_final': set_efc_final,
    #           }, 
    #     sai: {'set_state': set_sai_state,
    #           'set_initial': set_sai_initial,
    #           'set_final': set_sai_final,
    #          },
    #     unmet: {'set_state': set_unmet_state,
    #           'set_initial': set_unmet_initial,
    #           'set_final': set_unmet_final,
    #          },
    #     merit: {'set_state': set_merit_state,
    #           'set_initial': set_merit_initial,
    #           'set_final': set_merit_final,
    #          },
    #     pell_plus: {'set_state': set_pell_plus_state,
    #           'set_initial': set_pell_plus_initial,
    #           'set_final': set_pell_plus_final,
    #          },
    #     race: {
    #         'state': set_race_state,
    #         'initial': set_race_initial,
    #         'final': set_race_final,
    #     },
    #     age: {
    #         'state': set_age_state,
    #         'initial': set_age_initial,
    #         'final': set_age_final,
    #     },
    #     gender: {
    #         'state': set_gender_state,
    #         'initial': set_gender_initial,
    #         'final': set_gender_final,
    #     },
    #     pronouns: {
    #         'state': set_pronoun_state,
    #         'initial': set_pronoun_initial,
    #         'final': set_pronoun_final,
    #     },
    # 	gpa: {
    # 		'state': set_gpa_state,
    # 		'initial': set_gpa_initial,
    # 		'final': set_gpa_final,
    # 	},
    # 	scores: {
    # 		'state': set_scores_state,
    # 		'initial': set_scores_initial,
    # 		'final': set_scores_final,
    # 	},
    # 	midterms: {
    # 		'state': set_midterms_state,
    # 		'initial': set_midterms_initial,
    # 		'final': set_midterms_final,
    # 	},
    # 	epr: {
    # 		'state': set_epr_state,
    # 		'initial': set_epr_initial,
    # 		'final': set_epr_final,
    # 	},
    # 	printer: {
    # 		'state': set_printer_state,
    # 		'initial': set_printer_initial,
    # 		'final': set_printer_final,
    # 	},
    # 	legacy: {
    # 		'state': set_legacy_state,
    # 		'initial': set_legacy_initial,
    # 		'final': set_legacy_final,
    # 	},
    # 	athlete: {
    # 		'state': set_athlete_state,
    # 		'initial': set_athlete_initial,
    # 		'final': set_athlete_final,
    # 	},
    # 	firstgen: {
    # 		'state': set_firstgen_state,
    # 		'initial': set_firstgen_initial,
    # 		'final': set_firstgen_final,
    # 	},
    # 	distance: {
    # 		'state': set_distance_state,
    # 		'initial': set_distance_initial,
    # 		'final': set_distance_final,
    # 	},
    # 	credits: {
    # 		'state': set_credits_state,
    # 		'initial': set_credits_initial,
    # 		'final': set_credits_final,
    # 	},
    # 	housing: {
    # 		'state': set_housing_state,
    # 		'initial': set_housing_initial,
    # 		'final': set_housing_final,
    # 	},
    # 	residency: {
    # 		'state': set_residency_state,
    # 		'initial': set_residency_initial,
    # 		'final': set_residency_final,
    # 	},
    # 	origins: {
    # 		'state': set_origins_state,
    # 		'initial': set_origins_initial,
    # 		'final': set_origins_final,
    # 	},
    # 	transfer: {
    # 		'state': set_transfer_state,
    # 		'initial': set_transfer_initial,
    # 		'final': set_transfer_final,
    # 	},
    # 	extracurricular: {
    # 		'state': set_extracurricular_state,
    # 		'initial': set_extracurricular_initial,
    # 		'final': set_extracurricular_final,
    # 	},
    # 	wi_fi: {
    # 		'state': set_wi_fi_state,
    # 		'initial': set_wi_fi_initial,
    # 		'final': set_wi_fi_final,
    # 	},
    # }
    return (
        age,
        athlete,
        credits,
        distance,
        efc,
        epr,
        extracurricular,
        firstgen,
        gender,
        gpa,
        housing,
        legacy,
        merit,
        midterms,
        origins,
        pell,
        pell_plus,
        printer,
        pronouns,
        race,
        residency,
        sai,
        scores,
        transfer,
        unmet,
        wi_fi,
    )


@app.cell
def _(
    age,
    athlete,
    credits,
    distance,
    efc,
    epr,
    extracurricular,
    firstgen,
    gender,
    get_age_final,
    get_age_initial,
    get_age_state,
    get_athlete_final,
    get_athlete_initial,
    get_athlete_state,
    get_credits_final,
    get_credits_initial,
    get_credits_state,
    get_distance_final,
    get_distance_initial,
    get_distance_state,
    get_efc_final,
    get_efc_initial,
    get_efc_state,
    get_epr_final,
    get_epr_initial,
    get_epr_state,
    get_extracurricular_final,
    get_extracurricular_initial,
    get_extracurricular_state,
    get_firstgen_final,
    get_firstgen_initial,
    get_firstgen_state,
    get_gender_final,
    get_gender_initial,
    get_gender_state,
    get_gpa_final,
    get_gpa_initial,
    get_gpa_state,
    get_housing_final,
    get_housing_initial,
    get_housing_state,
    get_legacy_final,
    get_legacy_initial,
    get_legacy_state,
    get_merit_final,
    get_merit_initial,
    get_merit_state,
    get_midterms_final,
    get_midterms_initial,
    get_midterms_state,
    get_origins_final,
    get_origins_initial,
    get_origins_state,
    get_pell_final,
    get_pell_initial,
    get_pell_plus_final,
    get_pell_plus_initial,
    get_pell_plus_state,
    get_pell_state,
    get_printer_final,
    get_printer_initial,
    get_printer_state,
    get_pronoun_final,
    get_pronoun_initial,
    get_pronoun_state,
    get_race_final,
    get_race_initial,
    get_race_state,
    get_residency_final,
    get_residency_initial,
    get_residency_state,
    get_sai_final,
    get_sai_initial,
    get_sai_state,
    get_scores_final,
    get_scores_initial,
    get_scores_state,
    get_transfer_final,
    get_transfer_initial,
    get_transfer_state,
    get_unmet_final,
    get_unmet_initial,
    get_unmet_state,
    get_wi_fi_final,
    get_wi_fi_initial,
    get_wi_fi_state,
    gpa,
    housing,
    legacy,
    merit,
    midterms,
    origins,
    pell,
    pell_plus,
    printer,
    pronouns,
    race,
    residency,
    sai,
    scores,
    transfer,
    unmet,
    wi_fi,
):
    getters = {
        pell: {
            'state': get_pell_state(),
            'initial': get_pell_initial(),
            'final': get_pell_final(),
        },
        efc: {
            'state': get_efc_state(),
            'initial': get_efc_initial(),
            'final': get_efc_final(),
        },
        sai: {
            'state': get_sai_state(),
            'initial': get_sai_initial(),
            'final': get_sai_final(),
        },
        unmet: {
            'state': get_unmet_state(),
            'initial': get_unmet_initial(),
            'final': get_unmet_final(),
        },
        merit: {
            'state': get_merit_state(),
            'initial': get_merit_initial(),
            'final': get_merit_final(),
        },
        pell_plus: {
            'state': get_pell_plus_state(),
            'initial': get_pell_plus_initial(),
            'final': get_pell_plus_final(),
        },
        race: {
            'state': get_race_state(),
            'initial': get_race_initial(),
            'final': get_race_final(),
        },
        age: {
            'state': get_age_state(),
            'initial': get_age_initial(),
            'final': get_age_final(),
        },
        gender: {
            'state': get_gender_state(),
            'initial': get_gender_initial(),
            'final': get_gender_final(),
        },
        pronouns: {
            'state': get_pronoun_state(),
            'initial': get_pronoun_initial(),
            'final': get_pronoun_final(),
        },
        gpa: {
            'state': get_gpa_state(),
            'initial': get_gpa_initial(),
            'final': get_gpa_final(),
        },
        scores: {
            'state': get_scores_state(),
            'initial': get_scores_initial(),
            'final': get_scores_final(),
        },
        midterms: {
            'state': get_midterms_state(),
            'initial': get_midterms_initial(),
            'final': get_midterms_final(),
        },
        epr: {
            'state': get_epr_state(),
            'initial': get_epr_initial(),
            'final': get_epr_final(),
        },
        printer: {
            'state': get_printer_state(),
            'initial': get_printer_initial(),
            'final': get_printer_final(),
        },
        legacy: {
            'state': get_legacy_state(),
            'initial': get_legacy_initial(),
            'final': get_legacy_final(),
        },
        athlete: {
            'state': get_athlete_state(),
            'initial': get_athlete_initial(),
            'final': get_athlete_final(),
        },
        firstgen: {
            'state': get_firstgen_state(),
            'initial': get_firstgen_initial(),
            'final': get_firstgen_final(),
        },
        distance: {
            'state': get_distance_state(),
            'initial': get_distance_initial(),
            'final': get_distance_final(),
        },
        credits: {
            'state': get_credits_state(),
            'initial': get_credits_initial(),
            'final': get_credits_final(),
        },
        housing: {
            'state': get_housing_state(),
            'initial': get_housing_initial(),
            'final': get_housing_final(),
        },
        residency: {
            'state': get_residency_state(),
            'initial': get_residency_initial(),
            'final': get_residency_final(),
        },
        origins: {
            'state': get_origins_state(),
            'initial': get_origins_initial(),
            'final': get_origins_final(),
        },
        transfer: {
            'state': get_transfer_state(),
            'initial': get_transfer_initial(),
            'final': get_transfer_final(),
        },
        extracurricular: {
            'state': get_extracurricular_state(),
            'initial': get_extracurricular_initial(),
            'final': get_extracurricular_final(),
        },
        wi_fi: {
            'state': get_wi_fi_state(),
            'initial': get_wi_fi_initial(),
            'final': get_wi_fi_final(),
        },
    }
    return (getters,)


@app.cell(hide_code=True)
def variable_details(correct):
    variable_details = {
        'pell': {
            'title': 'Pell Status',
            'def': 'Whether a student receives a federal Pell Grant. New regulations restrict use of financial-aid data' 
                   'in predictive modeling.',
            'feedback': {
                'initial': {
                    'include': 'Including Pell Status violates current federal guidance and may expose the institution to penalties.'
                               'Consider aggregate reporting instead of individual-level use.',
                    'exclude': correct,
                    'other': 'Flagged',
                },
                'final': {
                    'include': "Including Pell Status violates current federal guidance and may expose the institution to penalties. "
                               "Consider aggregate reporting instead of individual-level use.",
                    'exclude': correct,
                    'other': correct,
                }
            },
        },
        'efc': {
            'title': 'Expected Family Contribution (EFC)',
            'def':  'Amount a family is expected to contribute to education costs (legacy FAFSA metric). '
                    'Regulatory compliance requires excluding this sensitive financial information.',
            'feedback': {
                'initial': {
                    'include': 'EFC is explicitly barred under 2024 Department of Education rules; '
                               'its inclusion would render the model non-compliant.',
                    'exclude': correct, 
                    'other': 'Flagged',
                },
                'final': {
                    'include': "EFC is explicitly barred under 2024 Department of Education rules; "
                               "its inclusion would render the model non-compliant.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'sai': {
            'title': "Student Aid Index (SAI)",
            'def': "A new metric from recent FAFSA changes that replaced EFC. "
                   "Recent implementation means this data may not be available for all students in your historical dataset.",
            'feedback': {
                'initial': {
                    'include': 'SAI is sensitive financial-aid data with incomplete coverage. Using it risks privacy '
                               'violations and injects missing-data bias.',
                    'exclude': correct,
                    'other': 'Flagged',
                },
                'final': {
                    'include': "SAI is sensitive financial-aid data with incomplete coverage. "
                               "Using it risks privacy violations and injects missing-data bias.",
                    'exclude': correct,
                    'other': correct,                
                },
            },
        },
        'unmet': {
            'title': "Unmet Need",
            'def': 'Gap between the cost of attendance and the student’s available resources. '
                   'Financial-stress indicator, but regulatory restrictions likely prohibit its use in individual-level models.',
            'feedback': {
                'initial': {
                    'include': 'Unmet Need combines multiple restricted data points. '
                               'Including it would contravene policy and amplify socioeconomic bias.',
                    'exclude': correct,
                    'other': 'Flagged',
                },
                'final': {
                    'include': "Unmet Need combines multiple restricted data points. "
                               "Including it would contravene policy and amplify socioeconomic bias.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'merit': {
            'title': "Merit Award Amount",
            'def': 'Scholarship amounts awarded based on academic achievement rather than financial need. '
                   'Consider whether this variable primarily reflects prior achievement or introduces '
                   'socioeconomic factors into your model.',            
            'feedback': {
                'initial': {
                    'include': 'Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. '
                               'Use only with a strong equity justification.',
                    'exclude': correct,
                    'other': 'Flagged',
                },
                'final': {
                    'include': "Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. "
                               "Use only with a strong equity justification.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'pell_plus': {
            'title': "Pell Plus",
            'def': 'University matching funds that complement federal Pell Grants. '
                   'Financial-aid variables like this are likely subject to the same regulatory restrictions '
                   'as other financial data.',
            'feedback': {
                'initial': {
                    'include': 'Pell Plus directly signals Pell participation; individual-level use is restricted. '
                               'Exclude or seek explicit legal clearance.',
                    'exclude': correct,
                    'other': 'Flagged',
                },
                'final': {
                    'include': "Pell Plus directly signals Pell participation; individual-level use is restricted. "
                               "Exclude or seek explicit legal clearance.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'race': {
            'title': "Race",
            'def': "Student’s self-reported racial/ethnic identity. Used during exploratory data analysis "
                   "but removed before predictive modeling.",
            'feedback': {
                'initial': {
                    'include': "Using Race as a predictive feature can embed historical inequities and violate institutional policy. "
                               "Retain only for bias-audit.",
                    'exclude': "Without Race you lose the ability to audit fair outcomes across groups. "
                               "Best practice is to keep it for auditing while excluding it from model training.",
                    'other': correct,
                },
                'final': {
                    'include': "Using Race as a predictive feature can embed historical inequities and violate institutional policy. "
                               "Retain only for bias-audit.",
                    'exclude': "Without Race you lose the ability to audit fair outcomes across groups. "
                               "Best practice is to keep it for auditing while excluding it from model training.",
                    'other': correct,
                },
            },
        },
        'gender': {
            'title': "Gender",
            'def': "Student’s gender identity as reported during application. "
                   "Protected class variable that raises ethical considerations.",
            'feedback': {
                'initial': {
                    'include': "Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention.",
                    'exclude': "Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs.",
                    'other': correct,
                },
                'final': {
                    'include': "Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention.",
                    'exclude': "Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs.",
                    'other': correct,
                },
            },
        },
        'age': {
            'title': "Age",
            'def': "Student’s age at enrollment. Flagged as protected class variable. "
                   "Consider whether age-based predictions might disadvantage non-traditional students while recognizing "
                   "that age can reflect meaningful differences in life circumstances.",
            'feedback': {
                'initial': {
                    'include': "Age may correlate with persistence but also with protected status (non-traditional learners). "
                               "Document equity safeguards or shift to audit-only use.",
                    'exclude': "Excluding Age erases patterns relevant to adult learners and hampers fairness checks. "
                               "Audit-only use is often a balanced choice.",
                    'other': correct,
                },
                'final': {
                    'include': "Age may correlate with persistence but also with protected status (non-traditional learners). "
                               "Document equity safeguards or shift to audit-only use.",
                    'exclude': "Excluding Age erases patterns relevant to adult learners and hampers fairness checks. "
                               "Audit-only use is often a balanced choice.",
                    'other': correct,
                },
            },
        },
        'pronouns': {
            'title': "Preferred Pronouns",
            'def': "Student-provided pronoun preference collected by campus climate office. "
                   "Optional field with high missingness. Can affirm identity but is not a stable predictor of retention.",
            'feedback': {
                'initial': {
                    'include': "Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. "
                               "Exclude or store only for awareness training, not analytics.",
                    'exclude': correct,
                    'other': "Pronoun data lack completeness and standardization, limiting audit utility. "
                             "Exclusion is usually appropriate.",
                },
                'final': {
                    'include': "Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. "
                               "Exclude or store only for awareness training, not analytics.",
                    'exclude': "Pronoun data lack completeness and standardization, limiting audit utility. "
                               "Exclusion is usually appropriate.",
                    'other': correct,
                },
            },
        },
        'gpa': {
            'title': "High School GPA",
            'def': "Student’s high-school grade-point average, a common predictor of college success. "
                   "This variable was unreliable due to reporting unreliability across high schools.",
            'feedback': {
                'initial': {
                    'include': "High-school GPAs lack standardisation; predictive value may be swamped by noise. "
                               "Consider excluding or flagging for quality remediation.",
                    'exclude': "Removing High-School GPA sacrifices a widely used predictor. "
                               "Could a scaled or percentile version salvage reliability?",
                    'other': correct,
                },
                'final': {
                    'include': "High-school GPAs lack standardisation; predictive value may be swamped by noise. "
                               "Consider excluding or flagging for quality remediation.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'scores': {
            'title': "Test Scores",
            'def': "Academic performance metrics from high school and standardised tests (SAT/ACT). "
                   "Due to test-optional policies implemented during COVID, scores may be missing for many students. "
                   "Creative solution to transform into a ‘test score submitted’ indicator leverages available "
                   "information while addressing systematic gaps.",
            'feedback': {
                'initial': {
                    'include': "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. "
                               "A submission indicator or audit flag may be safer.",
                    'exclude': "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. "
                               "Could you retain a binary ‘submitted’ flag instead?",
                    'other': correct,
                },
                'final': {
                    'include': "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. "
                               "A submission indicator or audit flag may be safer.",
                    'exclude': "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. "
                               "Could you retain a binary ‘submitted’ flag instead?",
                    'other': correct,
                },
            },
        },
        'midterms': {
            'title': "Midterm Grades",
            'def': "Preliminary academic performance indicators halfway through the term. "
                   "Identified as valuable but not consistently available across courses.",
            'feedback': {
                'initial': {
                    'include': "Mid-Term Grades appear only for certain courses, risking departmental bias. "
                               "Flag for quality improvement or exclude.",
                    'exclude': "Excluding Mid-Term Grades forfeits early academic-performance insight. "
                               "Could selective inclusion or data-quality work make it viable?",
                    'other': correct,
                },
                'final': {
                    'include': "Mid-Term Grades appear only for certain courses, risking departmental bias. "
                               "Flag for quality improvement or exclude.",
                    'exclude': "Excluding Mid-Term Grades forfeits early academic-performance insight. "
                               "Could selective inclusion or data-quality work make it viable?",
                    'other': correct,
                },
            },
        },
        'epr': {
            'title': "Early Progress Reports",
            'def': "Faculty-submitted assessments of student performance early in the semester. "
                   "Reporting inconsistency means this potentially valuable early-warning indicator isn’t reliable enough "
                   "to include.",
            'feedback': {
                'initial': {
                    'include': "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion.",
                    'exclude': "You lose a proven early-alert signal. Engage stakeholders to improve reporting rather "
                               "than discard entirely.",
                    'other': correct,
                },
                'final': {
                    'include': "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion.",
                    'exclude': "You lose a proven early-alert signal. "
                               "Engage stakeholders to improve reporting rather than discard entirely.",
                    'other': correct,
                },
            },
        },
        'printer': {
            'title': "Dorm Printer Usage",
            'def': "Weekly count of pages printed in residence-hall printers. "
                   "Logs are missing whenever printers are offline; many students use personal or library printers instead.",
            'feedback': {
                'initial': {
                    'include': "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. "
                               "Little theoretical link to persistence.",
                    'exclude': "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost.",
                    'other': "Appropriate—the variable is weakly linked to retention and suffers systemic gaps.",
                },
                'final': {
                    'include': "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. "
                               "Little theoretical link to persistence.",
                    'exclude': correct,
                    'other': "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost.",
                },
            },
        },
        'legacy': {
            'title': "Legacy Status",
            'def': "Whether the student has family members who previously attended the university. "
                   "May indicate stronger institutional ties.",
            'feedback': {
                'initial': {
                    'include': "Legacy Status may encode privilege and could unfairly prioritise well-connected students. "
                               "Document why its predictive gain outweighs equity concerns.",
                    'exclude': "You removed a factor linked to institutional attachment. "
                               "Could advisors design fair interventions if they knew a student lacked legacy ties?",
                    'other': correct,
                },
                'final': {
                    'include': "Legacy Status may encode privilege and could unfairly prioritise well-connected students. "
                               "Document why its predictive gain outweighs equity concerns.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'athlete': {
            'title': "Student Athlete Status",
            'def': "Whether the student participates in university athletics. "
                   "May indicate additional support structures but also time commitments.",
            'feedback': {
                'initial': {
                    'include': "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. "
                               "Ensure interventions add value.",
                    'exclude': "Athletes juggle academics and sport travel. "
                               "Excluding this variable may hide a known risk group lacking time for coursework.",
                    'other': correct,
                },
                'final': {
                    'include': "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. "
                               "Ensure interventions add value.",
                    'exclude': "Athletes juggle academics and sport travel. "
                               "Excluding this variable may hide a known risk group lacking time for coursework.",
                    'other': correct,
                },
            },
        },
        'firstgen': {
            'title': "First Generation Status",
            'def': "Indicates if the student is the first in their family to attend college; "
                   "may reflect differences in familiarity with college processes.",
            'feedback': {
                'initial': {
                    'include': "Good call—first-gen status supports equity-minded outreach. "
                               "Be sure to explain positive, not deficit-based, interventions.",
                    'exclude': "First-generation students often benefit from navigational support. "
                               "Omitting this variable could undermine equity goals.",
                    'other': correct,
                },
                'final': {
                    'include': "Good call—first-gen status supports equity-minded outreach. "
                               "Be sure to explain positive, not deficit-based, interventions.",
                    'exclude': "First-generation students often benefit from navigational support. "
                               "Omitting this variable could undermine equity goals.",
                    'other': correct,
                },
            },
        },
        'distance': {
            'title': "Distance From Home",
            'def': "Calculated metric based on student’s home address and campus location; "
                   "privacy-preserving alternative to ZIP codes.",
            'feedback': {
                'initial': {
                    'include': "Distance correlates with homesickness and travel cost but offers limited intervention levers. "
                               "Note whether actionable support exists (e.g., travel grants).",
                    'exclude': "Ignoring Distance removes insight into geographically isolated students "
                               "who may need community-building initiatives.",
                    'other': correct,
                },
                'final': {
                    'include': "Distance correlates with homesickness and travel cost but offers limited intervention levers. "
                               "Note whether actionable support exists (e.g., travel grants).",
                    'exclude': "Ignoring Distance removes insight into geographically isolated students "
                               "who may need community-building initiatives.",
                    'other': correct,
                },
            },
        },
        'credits': {
            'title': "Credits After Add/Drop",
            'def': "Credit hours the student is taking after the official add/drop deadline; "
                   "may reflect adjustment to academic realities.",
            'feedback': {
                'initial': {
                    'include': "Strong early signal of load management issues. Advisors can act quickly—solid choice.",
                    'exclude': "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value.",
                    'other': correct,
                },
                'final': {
                    'include': "Strong early signal of load management issues. Advisors can act quickly—solid choice.",
                    'exclude': "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value.",
                    'other': correct,
                },
            },
        },
        'housing': {
            'title': "Live On Campus or Commuter",
            'def': "Housing status affects integration into campus life and access to resources.",
            'feedback': {
                'initial': {
                    'include': "Useful and actionable—commuters may need remote-friendly support. "
                               "Ensure interventions respect time and travel constraints.",
                    'exclude': "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk.",
                    'other': correct,
                },
                'final': {
                    'include': "Useful and actionable—commuters may need remote-friendly support. "
                               "Ensure interventions respect time and travel constraints.",
                    'exclude': "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk.",
                    'other': correct,
                },
            },
        },
        'residency': {
            'title': "Residency (In-State / Out-of-State / International)",
            'def': "Affects tuition rates and connection to campus.",
            'feedback': {
                'initial': {
                    'include': "Residency drives cost burden; "
                               "interventions must avoid stereotyping out-of-state students as less committed.",
                    'exclude': "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups.",
                    'other': correct,
                },
                'final': {
                    'include': "Residency drives cost burden; "
                               "interventions must avoid stereotyping out-of-state students as less committed.",
                    'exclude': "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups.",
                    'other': correct,
                },
            },
        },
        'origins': {
            'title': "Urban / Rural / Suburban Origins",
            'def': "Classification of student’s home community; derived from heuristics.",
            'feedback': {
                'initial': {
                    'include': "Heuristic classification may mislabel students; validate definitions or risk noisy signals.",
                    'exclude': "Campus adjustment often differs by origin. "
                               "Excluding could overlook rural-to-urban transition challenges.",
                    'other': correct,
                },
                'final': {
                    'include': "Heuristic classification may mislabel students; validate definitions or risk noisy signals.",
                    'exclude': "Campus adjustment often differs by origin. "
                               "Excluding could overlook rural-to-urban transition challenges.",
                    'other': correct,
                },
            },
        },
        'transfer': {
            'title': "Transfer Status",
            'def': "Whether the student transferred from another institution versus starting as a first-year.",
            'feedback': {
                'initial': {
                    'include': "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant.",
                    'exclude': "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support.",
                    'other': correct,
                },
                'final': {
                    'include': "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant.",
                    'exclude': "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support.",
                    'other': correct,
                },
            },
        },
        'extracurricular': {
            'title': "Extracurricular Involvement",
            'def': "Participation in clubs or other non-academic activities; data collection relies on self-reporting.",
            'feedback': {
                'initial': {
                    'include': "Self-report bias and missingness limit reliability; "
                               "document caveats to avoid overstating predictive value.",
                    'exclude': "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright.",
                    'other': correct,
                },
                'final': {
                    'include': "Self-report bias and missingness limit reliability; "
                               "document caveats to avoid overstating predictive value.",
                    'exclude': "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright.",
                    'other': correct,
                },
            },
        },
        'wi_fi': {
            'title': "Campus-Wi-Fi Gaming Network Participation",
            'def': "Binary flag—student devices connected to high-traffic gaming ports for ≥ 5 hours/week during evenings.",
            'feedback': {
                'initial': {
                    'include': "Correlation to retention unproven; risk of pathologising hobby behaviour. "
                               "Provide theoretical justification or exclude.",
                    'exclude': "Sensible—no established link to academic persistence.",
                    'other': correct,
                },
                'final': {
                    'include': "Correlation to retention unproven; risk of pathologising hobby behaviour. "
                               "Provide theoretical justification or exclude.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
    }
    return (variable_details,)


@app.cell(hide_code=True)
def flow_management(mo):
    #state getters and setters
    continue_to_task_2, set_continue_to_task_2 = mo.state(False)
    continue_to_task_3, set_continue_to_task_3 = mo.state(False)
    continue_to_task_4, set_continue_to_task_4 = mo.state(False)
    continue_to_final_check, set_continue_to_final_check = mo.state(False)
    continue_to_final_feedback, set_continue_to_final_feedback = mo.state(False)
    return (
        continue_to_final_check,
        continue_to_final_feedback,
        continue_to_task_2,
        continue_to_task_3,
        continue_to_task_4,
        set_continue_to_final_check,
        set_continue_to_task_2,
        set_continue_to_task_3,
        set_continue_to_task_4,
    )


@app.cell
def _(
    continue_to_task_2,
    mo,
    set_continue_to_final_check,
    set_continue_to_task_2,
    set_continue_to_task_3,
    set_continue_to_task_4,
):
    def update_flow_buttons(setter): 
        setter(True)
        continue_to_task_2()

    #continue buttons
    launch_task_2 = mo.ui.run_button(label="Continue to Task 2", on_change=set_continue_to_task_2(True)).center()

    launch_task_3 = mo.ui.button(label="Continue to Task 3", on_click=lambda _: update_flow_buttons(set_continue_to_task_3)).center()
    launch_task_4 = mo.ui.button(label="Continue to Task 4", on_click=lambda _: update_flow_buttons(set_continue_to_task_4)).center()
    launch_final_check = mo.ui.button(label="Continue to Final Check", 
                                      on_click=lambda _: update_flow_buttons(set_continue_to_final_check)).center()
    launch_final_feedback = mo.ui.button(label="Continue to Final Feedback", 
                                         on_click=lambda _: update_flow_buttons(set_continue_to_final_check)).center()
    return launch_task_2, launch_task_3


@app.cell
def reactive_elements_and_states(mo):
    #task 1 getters and setters
    get_pell_state, set_pell_state = mo.state(None)
    get_efc_state, set_efc_state = mo.state(None)
    get_sai_state, set_sai_state = mo.state(None)
    get_unmet_state, set_unmet_state = mo.state(None)
    get_merit_state, set_merit_state = mo.state(None)
    get_pell_plus_state, set_pell_plus_state = mo.state(None)

    #task 2

    #getters and setters
    get_race_state, set_race_state = mo.state(None)
    get_gender_state, set_gender_state = mo.state(None)
    get_age_state, set_age_state = mo.state(None)
    get_pronoun_state, set_pronoun_state = mo.state(None)


    #task_3

    #getters and setters
    get_gpa_state, set_gpa_state = mo.state(None)
    get_scores_state, set_scores_state = mo.state(None)
    get_midterms_state, set_midterms_state = mo.state(None)
    get_epr_state, set_epr_state = mo.state(None)
    get_printer_state, set_printer_state = mo.state(None)

    #task_4

    #getters_and_setters
    get_legacy_state, set_legacy_state = mo.state(None)
    get_athlete_state, set_athlete_state = mo.state(None)
    get_firstgen_state, set_firstgen_state = mo.state(None)
    get_distance_state, set_distance_state = mo.state(None)
    get_credits_state, set_credits_state = mo.state(None)
    get_housing_state, set_housing_state = mo.state(None)
    get_residency_state, set_residency_state = mo.state(None)
    get_origins_state, set_origins_state = mo.state(None)
    get_transfer_state, set_transfer_state = mo.state(None)
    get_extracurricular_state, set_extracurricular_state = mo.state(None)
    get_wi_fi_state, set_wi_fi_state = mo.state(None)

    #feedback getters and setters
    get_pell_initial, set_pell_initial = mo.state(None)
    get_pell_final, set_pell_final = mo.state(None)
    get_efc_initial, set_efc_initial = mo.state(None)
    get_efc_final, set_efc_final = mo.state(None)
    get_sai_initial, set_sai_initial = mo.state(None)
    get_sai_final, set_sai_final = mo.state(None)
    get_unmet_initial, set_unmet_initial = mo.state(None)
    get_unmet_final, set_unmet_final = mo.state(None)
    get_merit_initial, set_merit_initial = mo.state(None)
    get_merit_final, set_merit_final = mo.state(None)
    get_pell_plus_initial, set_pell_plus_initial = mo.state(None)
    get_pell_plus_final, set_pell_plus_final = mo.state(None)
    get_race_initial, set_race_initial = mo.state(None)
    get_race_final, set_race_final = mo.state(None)
    get_gender_initial, set_gender_initial = mo.state(None)
    get_gender_final, set_gender_final = mo.state(None)
    get_age_initial, set_age_initial = mo.state(None)
    get_age_final, set_age_final = mo.state(None)
    get_pronoun_initial, set_pronoun_initial = mo.state(None)
    get_pronoun_final, set_pronoun_final = mo.state(None)
    get_gpa_initial, set_gpa_initial = mo.state(None)
    get_gpa_final, set_gpa_final = mo.state(None)
    get_scores_initial, set_scores_initial = mo.state(None)
    get_scores_final, set_scores_final = mo.state(None)
    get_midterms_initial, set_midterms_initial = mo.state(None)
    get_midterms_final, set_midterms_final = mo.state(None)
    get_epr_initial, set_epr_initial = mo.state(None)
    get_epr_final, set_epr_final = mo.state(None)
    get_printer_initial, set_printer_initial = mo.state(None)
    get_printer_final, set_printer_final = mo.state(None)
    get_legacy_initial, set_legacy_initial = mo.state(None)
    get_legacy_final, set_legacy_final = mo.state(None)
    get_athlete_initial, set_athlete_initial = mo.state(None)
    get_athlete_final, set_athlete_final = mo.state(None)
    get_firstgen_initial, set_firstgen_initial = mo.state(None)
    get_firstgen_final, set_firstgen_final = mo.state(None)
    get_distance_initial, set_distance_initial = mo.state(None)
    get_distance_final, set_distance_final = mo.state(None)
    get_credits_initial, set_credits_initial = mo.state(None)
    get_credits_final, set_credits_final = mo.state(None)
    get_housing_initial, set_housing_initial = mo.state(None)
    get_housing_final, set_housing_final = mo.state(None)
    get_residency_initial, set_residency_initial = mo.state(None)
    get_residency_final, set_residency_final = mo.state(None)
    get_origins_initial, set_origins_initial = mo.state(None)
    get_origins_final, set_origins_final = mo.state(None)
    get_transfer_initial, set_transfer_initial = mo.state(None)
    get_transfer_final, set_transfer_final = mo.state(None)
    get_extracurricular_initial, set_extracurricular_initial = mo.state(None)
    get_extracurricular_final, set_extracurricular_final = mo.state(None)
    get_wi_fi_initial, set_wi_fi_initial = mo.state(None)
    get_wi_fi_final, set_wi_fi_final = mo.state(None)
    return (
        get_age_final,
        get_age_initial,
        get_age_state,
        get_athlete_final,
        get_athlete_initial,
        get_athlete_state,
        get_credits_final,
        get_credits_initial,
        get_credits_state,
        get_distance_final,
        get_distance_initial,
        get_distance_state,
        get_efc_final,
        get_efc_initial,
        get_efc_state,
        get_epr_final,
        get_epr_initial,
        get_epr_state,
        get_extracurricular_final,
        get_extracurricular_initial,
        get_extracurricular_state,
        get_firstgen_final,
        get_firstgen_initial,
        get_firstgen_state,
        get_gender_final,
        get_gender_initial,
        get_gender_state,
        get_gpa_final,
        get_gpa_initial,
        get_gpa_state,
        get_housing_final,
        get_housing_initial,
        get_housing_state,
        get_legacy_final,
        get_legacy_initial,
        get_legacy_state,
        get_merit_final,
        get_merit_initial,
        get_merit_state,
        get_midterms_final,
        get_midterms_initial,
        get_midterms_state,
        get_origins_final,
        get_origins_initial,
        get_origins_state,
        get_pell_final,
        get_pell_initial,
        get_pell_plus_final,
        get_pell_plus_initial,
        get_pell_plus_state,
        get_pell_state,
        get_printer_final,
        get_printer_initial,
        get_printer_state,
        get_pronoun_final,
        get_pronoun_initial,
        get_pronoun_state,
        get_race_final,
        get_race_initial,
        get_race_state,
        get_residency_final,
        get_residency_initial,
        get_residency_state,
        get_sai_final,
        get_sai_initial,
        get_sai_state,
        get_scores_final,
        get_scores_initial,
        get_scores_state,
        get_transfer_final,
        get_transfer_initial,
        get_transfer_state,
        get_unmet_final,
        get_unmet_initial,
        get_unmet_state,
        get_wi_fi_final,
        get_wi_fi_initial,
        get_wi_fi_state,
        set_age_final,
        set_age_initial,
        set_age_state,
        set_athlete_final,
        set_athlete_initial,
        set_athlete_state,
        set_credits_final,
        set_credits_initial,
        set_credits_state,
        set_distance_final,
        set_distance_initial,
        set_distance_state,
        set_efc_final,
        set_efc_initial,
        set_efc_state,
        set_epr_final,
        set_epr_initial,
        set_epr_state,
        set_extracurricular_final,
        set_extracurricular_initial,
        set_extracurricular_state,
        set_firstgen_final,
        set_firstgen_initial,
        set_firstgen_state,
        set_gender_final,
        set_gender_initial,
        set_gender_state,
        set_gpa_final,
        set_gpa_initial,
        set_gpa_state,
        set_housing_final,
        set_housing_initial,
        set_housing_state,
        set_legacy_final,
        set_legacy_initial,
        set_legacy_state,
        set_merit_final,
        set_merit_initial,
        set_merit_state,
        set_midterms_final,
        set_midterms_initial,
        set_midterms_state,
        set_origins_final,
        set_origins_initial,
        set_origins_state,
        set_pell_final,
        set_pell_initial,
        set_pell_plus_final,
        set_pell_plus_initial,
        set_pell_plus_state,
        set_pell_state,
        set_printer_final,
        set_printer_initial,
        set_printer_state,
        set_pronoun_final,
        set_pronoun_initial,
        set_pronoun_state,
        set_race_final,
        set_race_initial,
        set_race_state,
        set_residency_final,
        set_residency_initial,
        set_residency_state,
        set_sai_final,
        set_sai_initial,
        set_sai_state,
        set_scores_final,
        set_scores_initial,
        set_scores_state,
        set_transfer_final,
        set_transfer_initial,
        set_transfer_state,
        set_unmet_final,
        set_unmet_initial,
        set_unmet_state,
        set_wi_fi_final,
        set_wi_fi_initial,
        set_wi_fi_state,
    )


@app.cell
def functions(correct, getters, mo, reactive_dict, variable_details):

    #functions
    def var_selection_text_generator(choice:str|None, task:int)->str: 
        if choice == 'include': 
            insert_text = "🟢 **Include** the variable **as-is**."
        elif choice == 'exclude':
            insert_text = "🔴 **Exclude** the variable **entirely**."
        elif choice == 'other': 
            if task==1: 
                insert_text = "🟡 **Flag** the variable **for Review**."
            elif task == 2: 
                insert_text = '🟠 **Keep** the variable **for Bias-Audit Only**.'
            elif task in [3, 4]: 
                insert_text = '🟠 **Flag** the variable **for Data-Quality Improvement**.'
        elif choice == 'exclude_unre': 
            insert_text = "🔴 **Exclude** the variable **due to unreliability**."
        else:
            insert_text = "⚪️ **not yet selected**"
            return f"You have {insert_text} a variable option."
        return f"You decided to {insert_text}"


    def process_task_variables(obj):
        content = mo.vstack([
            mo.md(obj.definition),
            mo.hstack([obj.incl, obj.excl, obj.flag])            
        ])
        output = mo.vstack([
            mo.accordion({obj.title: content}),
            mo.md(f"""{var_selection_text_generator(getters[obj]['state'], obj.task)}"""),
            obj.text if getters[obj]['state'] else ''
        ])
        return output


    def initial_variable_feedback(obj): 
        get = getters[obj]['state']
        response_text = getters[obj]['initial'] if get else ''
        feedback_out = mo.md(f"""**{obj.title}:** {response_text}""") 
        return feedback_out


    # def variable_selection_output(var:str): 
    #     reactives, text, getter = gather_variable_attributes(var)
    #     content = mo.vstack([
    #         mo.md(text['def']),
    #         mo.hstack([reactives['include'], reactives['exclude'], reactives['other']], gap='1rem'),
    #     ])
    #     reactives = reactive_dict[var]
    #     output = mo.vstack([
    #         mo.accordion({text['title']: content}),
    #         mo.md(f"""{var_selection_text_generator(getter)}"""),
    #         reactives['textbox'] if getter else ''
    #     ])
    #     return output


    def gather_variable_attributes(var:str):
        return reactive_dict[var], variable_details[var], reactive_dict[var]['getter']


    # def generate_feedback(var:str):
    #     reactives, text, getter = gather_variable_attributes(var) 
    #     if getter: 
    #         if getter in text['feedback']['initial']:
    #             feedback_message = text['feedback']['initial'][getter]
    #         else: 
    #             feedback_message = text['feedback']['initial']['other']
    #     else: 
    #         feedback_message = ''
    #     return mo.md(f"""**{text['title']}:** {feedback_message}""")


    def decision_label(choice):
        if choice in ["include", "include_as_is", "include_as-is"]:
            return "Include"
        elif choice in ["flag", "flag_improvement", "audit_only"]:
            return "Flag"
        elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
            return "Exclude"
        else:
            return "No Selection"


    def gather_final_feedback(var: str, correct_list: list[any], incorrect: list[any]):
        reactives, text, getter = gather_variable_attributes(var)
        title = text['title']
        if getter: 
            if getter not in ['include', 'exclude']: 
                getter = 'other'
            feedback = text['feedback']['final'][getter] 
            if feedback == correct:
                correct_list.append(title)
            else: 
                incorrect.append(mo.md(f"""**{title}**: {feedback}"""))
        else: 
            incorrect.append(mo.md(f"""**{title}**: No variable was selected."""))
        return correct_list, incorrect


    def format_final_feedback(correct: list[any], incorrect: list[any]): 
        corr_text = f"""✅ **No major concerns for:** {', '.join(correct)}""" if len(correct)>0 else ""
        corr_output = mo.md(corr_text)
        incorr_text = "⚠️ **At least one restricted variable still needs your attention.**" if len(incorrect)>0 else "✅ **Everything looks good in this wave!**"
        incorr_output = mo.md(incorr_text)
        final_output = mo.vstack([incorr_output] + incorrect + [corr_output])
        return final_output
    return (
        decision_label,
        format_final_feedback,
        gather_final_feedback,
        initial_variable_feedback,
        process_task_variables,
    )


@app.cell
def _():
    import marimo as mo                           
    mo.md(
        "# Variable selection scenario\n"

    )
    return (mo,)


@app.cell(hide_code=True)
def task_1(mo):
    mo.vstack(
        [
            # 1) subtitle
            mo.md("## The story so far"),

            # 2) “Note to the team”
            mo.md(
                "The university is a large research institution that competes for students in a crowded " \
                "higher-education market. Over the past five years the first-to-second-year retention rate has " \
                "drifted downward, and graduation timelines have lengthened. Senior leadership has asked the Office of " \
                "the Provost to treat student persistence as a strategic priority rather than a routine metric. " \
                "An internal mandate now calls for data-informed, proactive outreach so that support staff can offer " \
                "help long before a student considers leaving. Within the Office of the Provost a small Student Success Analytics " \
                "group has been established. This team combines institutional researchers, academic advisors, compliance officers, "
                "and data engineers. Its first assignment is to create an early warning intelligence tool that flags continuing " \
                "undergraduates who appear at risk of stopping out or falling behind schedule. Advisors will then contact those " \
                "students and connect them with tutoring, financial counseling, or mentoring. The analytics group is expected to " \
                "respect privacy regulations such as FERPA and recent federal guidance that limits the use of individual financial-aid " \
                "records in automated decision systems. It is also expected to uphold the university commitment to equity and transparency in " \
                "every technical choice."
            ),


            mo.md("&nbsp;"),

            mo.md("## Role"),

            # 2) “Note to the team”
            mo.md(
                "You serve as the team’s data science specialist. Your immediate task is not to build a model but to decide which " \
                "pieces of information should be fed into one. Working with colleagues you have assembled a data dictionary drawn " \
                "from the university warehouse. The dictionary lists common attributes such as high school grade point averages, " \
                "standardized test scores, race, gender, residency status, and course loads. It also contains financial indicators " \
                "like Pell eligibility and Expected Family Contribution. Several context-specific items are included as well."\
                "Examples are whether a student applied to a regional campus after a main-campus denial, whether a student is a varsity athlete,"\
                "and the distance between the student’s home address and campus. No raw records are available at this stage of the project;"\
                "only the variable descriptions, their known limitations, and any red-flag notes provided by legal or ethical reviewers."
            ),


            mo.md("&nbsp;"),


            mo.md("## Business Objective & Product"),

            # 2) “Note to the team”
            mo.md(
                "Academic advisors need a concise, defensible list of candidate predictors that can drive a predictive model without violating " \
                "regulations or undermining equitable treatment. Your deliverable for this scenario is a Variable Selection Brief. " \
                "In one page you will designate each variable as included, excluded, or flagged for additional discussion. " \
                "For every decision you will provide a short rationale that links back to the goals of privacy protection, fairness, and practical usefulness. " \
                "Advisors and compliance staff will review and sign this brief before any modelling work proceeds."
            ),


            mo.md("&nbsp;"),

            # 3) instructions for the table
            mo.md("## Task 1 Regulatory Gate"),
            mo.md("*For each variable choose **one** action:*"),

            # 4) centralized table
            mo.Html(
                """
                <div style="display:flex; justify-content:center;">
                  <table style="border-collapse:separate; border-spacing:0 6px; text-align:center;">
                    <thead>
                      <tr>
                        <th style="padding:0.5rem 1.5rem;">Action</th>
                        <th style="padding:0.5rem 1.5rem;">Meaning</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="padding:0.5rem 1.5rem;"><b>Include</b></td>
                        <td style="padding:0.5rem 1.5rem;">
                          Use this variable in the predictive model.
                        </td>
                      </tr>
                      <tr>
                        <td style="padding:0.5rem 1.5rem;"><b>Exclude</b></td>
                        <td style="padding:0.5rem 1.5rem;">
                          Remove it from consideration.
                        </td>
                      </tr>
                      <tr>
                        <td style="padding:0.5rem 1.5rem;"><b>Flag for Legal / IRB Review</b></td>
                        <td style="padding:0.5rem 1.5rem;">
                          Put the variable on hold until university counsel (or the IRB) provides guidance.
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            ),
        ]
    )
    return


@app.cell
def anchor_task_1(mo):
    mo.Html('<div id="task_1"></div>')
    return


@app.cell
def _(mo):
    mo.md("""
    ##come back here
    """)
    return


@app.cell
def _(mo, process_task_variables, variables_by_task):
    task_1_variable_selection = [process_task_variables(item) for item in variables_by_task[1]['variables']]

    mo.output.replace(mo.vstack(task_1_variable_selection))
    return


@app.cell
def _(initial_variable_feedback, mo, variables_by_task):
    task_1_feedback = [initial_variable_feedback(var) for var in variables_by_task[1]['variables']]

    content_detail_feedback = mo.vstack(task_1_feedback)

    mo.accordion({"Detailed Feedback": content_detail_feedback})
    return


@app.cell
def section_separator(mo):
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell
def _(launch_task_2):
    launch_task_2
    return


@app.cell
def anchor_task_2(mo):
    mo.Html('<div id="task_2"></div>')
    return


@app.cell(hide_code=True)
def task_2(continue_to_task_2, mo):
    mo.stop(not continue_to_task_2())

    mo.vstack([
        mo.md("## Task 2 – Protected-Attribute Gate: Fairness and Equity Check"),
        mo.md(
            "**Note to the learner**  \n"
            "This wave challenges you to balance fairness, inclusivity, and ethical use of sensitive personal attributes. "
            "The decision set differs from Wave 1: some attributes are useful for post-hoc bias auditing but risky inside a predictive model. "
            "You must decide how (or whether) to retain them."
        ),
        mo.md("&nbsp;"),
        mo.md("*For every variable choose **one** action:*"),
        mo.Html(
            """
            <div style="display:flex; justify-content:center;">
              <table style="border-collapse:separate; border-spacing:0 6px; text-align:center;">
                <thead>
                  <tr>
                    <th style="padding:0.5rem 1.5rem;">Stance</th>
                    <th style="padding:0.5rem 1.5rem;">Meaning</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Include as-is</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Feed directly into the predictive algorithm.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Keep for Bias-Audit Only</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Store alongside model outputs to test for disparate impact, but do not let the algorithm see it during training.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Exclude Entirely</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Do not collect or use in any form.
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            """
        ),
    ])
    return


@app.cell
def _(mo, process_task_variables, variables_by_task):
    task_2_variable_selection = [process_task_variables(item) for item in variables_by_task[2]['variables']]

    mo.output.replace(mo.vstack(task_2_variable_selection))
    return


@app.cell
def _(initial_variable_feedback, mo, variables_by_task):
    task_2_feedback = [initial_variable_feedback(var) for var in variables_by_task[2]['variables']]

    content_detail_feedback_2 = mo.vstack(task_2_feedback)

    mo.accordion({"Detailed Feedback": content_detail_feedback_2})
    return


@app.cell(hide_code=True)
def task_2_selections():
    # mo.stop(not continue_to_task_2())
    # task_2_display_output = [variable_selection_output(var) for var in variables_by_task[2]['variables']]

    # mo.output.replace(
    #     mo.vstack(task_2_display_output)
    # )
    return


@app.cell(hide_code=True)
def task_2_detailed_feedback():
    # mo.stop(not continue_to_task_2())
    # task_2_feedback = [generate_feedback(var) for var in variables_by_task[2]['variables']]

    # task_2_content_detail_feedback = mo.vstack(task_2_feedback)

    # mo.accordion({"Detailed Feedback": task_2_content_detail_feedback})
    return


@app.cell(hide_code=True)
def section_separator(continue_to_task_2, mo):
    mo.stop(not continue_to_task_2())
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell
def _(continue_to_task_2, launch_task_3, mo):
    mo.stop(not continue_to_task_2())
    launch_task_3
    return


@app.cell(hide_code=True)
def anchor_task_3(mo):
    mo.Html('<div id="task_3"></div>')
    return


@app.cell(hide_code=True)
def task_3(continue_to_task_3, mo):
    mo.stop(not continue_to_task_3())

    mo.vstack([
        mo.md("## Task 3 – Data-Reliability Gate: Data Quality, Context Awareness, and Proportionality"),
        mo.md(
            "**Note to the learner**  \n"
            "You now confront fields whose measurement error, missingness, or inconsistent collection raise doubts about usefulness. "
            "The Responsible-Data-Science principles at play are Data Quality, Context Awareness, and Proportionality "
            "(does the signal justify the noise?)."
        ),
        mo.md("&nbsp;"),
        mo.md("*For every variable choose **one** action:*"),
        mo.Html(
            """
            <div style="display:flex; justify-content:center;">
              <table style="border-collapse:separate; border-spacing:0 6px; text-align:center;">
                <thead>
                  <tr>
                    <th style="padding:0.5rem 1.5rem;">Action</th>
                    <th style="padding:0.5rem 1.5rem;">Meaning</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Include as-is</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Accept the quality caveats and feed the variable to the model.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Exclude (too unreliable)</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Remove the variable entirely.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Flag for Data-Quality Improvement</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Pause use until stakeholders can standardise collection or transform it into a more reliable proxy.
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            """
        ),
    ])
    return


@app.cell(hide_code=True)
def task_3_selections(
    continue_to_task_3,
    mo,
    variable_selection_output,
    variables_by_task,
):
    mo.stop(not continue_to_task_3())
    task_3_display_output = [variable_selection_output(var) for var in variables_by_task[3]['variables']]

    mo.output.replace(
        mo.vstack(task_3_display_output)
    )
    return


@app.cell(hide_code=True)
def task_3_detailed_feedback(
    continue_to_task_3,
    generate_feedback,
    mo,
    variables_by_task,
):
    mo.stop(not continue_to_task_3())

    task_3_feedback = [generate_feedback(var) for var in variables_by_task[3]['variables']]

    task_3_content_detail_feedback = mo.vstack(task_3_feedback)

    mo.accordion({"Detailed Feedback": task_3_content_detail_feedback})
    return


@app.cell(hide_code=True)
def section_separator(continue_to_task_3, mo):
    mo.stop(not continue_to_task_3())

    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell(hide_code=True)
def anchor_task_4(mo):
    mo.Html('<div id="task_4"></div>')
    return


@app.cell(hide_code=True)
def task_4(continue_to_task_4, mo):
    mo.stop(not continue_to_task_4())

    mo.vstack([
        mo.md("## Task 4 – Equity & Actionability Gate: Beneficence, Proportionality, and Transparency"),
        mo.md(
            "**Note to the learner**  \n"
            "The final wave asks you to decide whether potentially predictive, yet ethically fraught variables belong in the model. "
            "Emphasis shifts to Beneficence, Proportionality, and Transparency. You must weigh (a) predictive value against "
            "(b) ability to drive a fair, actionable intervention."
        ),
        mo.md("&nbsp;"),
        mo.md("*For every variable choose **one** action:*"),
        mo.Html(
            """
            <div style="display:flex; justify-content:center;">
              <table style="border-collapse:separate; border-spacing:0 6px; text-align:center;">
                <thead>
                  <tr>
                    <th style="padding:0.5rem 1.5rem;">Action</th>
                    <th style="padding:0.5rem 1.5rem;">Meaning</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Include as-is</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Accept the quality caveats and feed the variable to the model.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Exclude (too unreliable)</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Remove the variable entirely.
                    </td>
                  </tr>
                  <tr>
                    <td style="padding:0.5rem 1.5rem;"><b>Flag for Data-Quality Improvement</b></td>
                    <td style="padding:0.5rem 1.5rem;">
                      Pause use until stakeholders can standardise collection or transform it into a more reliable proxy.
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
            """
        ),
    ])
    return


@app.cell(hide_code=True)
def _():
    #keeping until I'm sure I can delete
    # task_4_variable_details = {
    #     'legacy': {
    #         'title': 'Legacy Status',
    #         'def': 'Whether the student has family members who previously attended the university. May indicate stronger institutional ties.',
    #         'feedback': {
    #             'include': 'Legacy Status may encode privilege and could unfairly prioritise well-connected students. Document why its predictive gain outweighs equity concerns.',
    #             'exclude': 'You removed a factor linked to institutional attachment. Could advisors design fair interventions if they knew a student lacked legacy ties?',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_legacy_choice(),
    #         'textbox': legacy_textbox,
    #         'buttons': {
    #             'include': legacy_incl,
    #             'exclude': legacy_excl,
    #             'other': legacy_flag,
    #         },
    #     },
    #     'athlete': {
    #         'title': 'Student Athlete Status',
    #         'def': 'Whether the student participates in university athletics. May indicate additional support structures but also time commitments.',
    #         'feedback': {
    #             'include': 'Athlete status already triggers dedicated advising; flagging athletes again may waste resources. Ensure interventions add value.',
    #             'exclude': 'Athletes juggle academics and sport travel. Excluding this variable may hide a known risk group lacking time for coursework.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_athlete_choice(),
    #         'textbox': athlete_textbox,
    #         'buttons': {
    #             'include': athlete_incl,
    #             'exclude': athlete_excl,
    #             'other': athlete_flag,
    #         },
    #     },
    #     'firstgen': {
    #         'title': 'First Generation Status',
    #         'def': 'Indicates if the student is the first in their family to attend college; may reflect differences in familiarity with college processes.',
    #         'feedback': {
    #             'include': 'Good call—first-gen status supports equity-minded outreach. Be sure to explain positive, not deficit-based, interventions.',
    #             'exclude': 'First-generation students often benefit from navigational support. Omitting this variable could undermine equity goals.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_firstgen_choice(),
    #         'textbox': firstgen_textbox,
    #         'buttons': {
    #             'include': firstgen_incl,
    #             'exclude': firstgen_excl,
    #             'other': firstgen_flag,
    #         },
    #     },
    #     'distance': {
    #         'title': 'Distance From Home',
    #         'def': 'Calculated metric based on student’s home address and campus location; privacy-preserving alternative to ZIP codes.',
    #         'feedback': {
    #             'include': 'Distance correlates with homesickness and travel cost but offers limited intervention levers. Note whether actionable support exists (e.g., travel grants).',
    #             'exclude': 'Ignoring Distance removes insight into geographically isolated students who may need community-building initiatives.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_distance_choice(),
    #         'textbox': distance_textbox,
    #         'buttons': {
    #             'include': distance_incl,
    #             'exclude': distance_excl,
    #             'other': distance_flag,
    #         },
    #     },
    #     'credits': {
    #         'title': 'Credits After Add/Drop',
    #         'def': 'Credit hours the student is taking after the official add/drop deadline; may reflect adjustment to academic realities.',
    #         'feedback': {
    #             'include': 'Strong early signal of load management issues. Advisors can act quickly—solid choice.',
    #             'exclude': 'Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_credits_choice(),
    #         'textbox': credits_textbox,
    #         'buttons': {
    #             'include': credits_incl,
    #             'exclude': credits_excl,
    #             'other': credits_flag,
    #         },
    #     },
    #     'housing': {
    #         'title': 'Live On Campus or Commuter',
    #         'def': 'Housing status affects integration into campus life and access to resources.',
    #         'feedback': {
    #             'include': 'Useful and actionable—commuters may need remote-friendly support. Ensure interventions respect time and travel constraints.',
    #             'exclude': 'Housing status strongly predicts engagement. Excluding it may mask differences in retention risk.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_housing_choice(),
    #         'textbox': housing_textbox,
    #         'buttons': {
    #             'include': housing_incl,
    #             'exclude': housing_excl,
    #             'other': housing_flag,
    #         },
    #     },
    #     'residency': {
    #         'title': 'Residency (In-State / Out-of-State / International)',
    #         'def': 'Affects tuition rates and connection to campus.',
    #         'feedback': {
    #             'include': 'Residency drives cost burden; interventions must avoid stereotyping out-of-state students as less committed.',
    #             'exclude': 'Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_residency_choice(),
    #         'textbox': residency_textbox,
    #         'buttons': {
    #             'include': residency_incl,
    #             'exclude': residency_excl,
    #             'other': residency_flag,
    #         },
    #     },
    #     'origins': {
    #         'title': 'Urban / Rural / Suburban Origins',
    #         'def': 'Classification of student’s home community; derived from heuristics.',
    #         'feedback': {
    #             'include': 'Heuristic classification may mislabel students; validate definitions or risk noisy signals.',
    #             'exclude': 'Campus adjustment often differs by origin. Excluding could overlook rural-to-urban transition challenges.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_origins_choice(),
    #         'textbox': origins_textbox,
    #         'buttons': {
    #             'include': origins_incl,
    #             'exclude': origins_excl,
    #             'other': origins_flag,
    #         },
    #     },
    #     'transfer': {
    #         'title': 'Transfer Status',
    #         'def': 'Whether the student transferred from another institution versus starting as a first-year.',
    #         'feedback': {
    #             'include': 'Transfer students face unique credit-articulation hurdles—actionable and equity-relevant.',
    #             'exclude': 'You dropped a key subgroup with elevated departure risk. Advisors may miss needed support.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_transfer_choice(),
    #         'textbox': transfer_textbox,
    #         'buttons': {
    #             'include': transfer_incl,
    #             'exclude': transfer_excl,
    #             'other': transfer_flag,
    #         },
    #     },
    #     'extracurricular': {
    #         'title': 'Extracurricular Involvement',
    #         'def': 'Participation in clubs or other non-academic activities; data collection relies on self-reporting.',
    #         'feedback': {
    #             'include': 'Self-report bias and missingness limit reliability; document caveats to avoid overstating predictive value.',
    #             'exclude': 'Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_extracurricular_choice(),
    #         'textbox': extracurricular_textbox,
    #         'buttons': {
    #             'include': extracurricular_incl,
    #             'exclude': extracurricular_excl,
    #             'other': extracurricular_flag,
    #         },
    #     },
    #     'wi_fi': {
    #         'title': 'Campus-Wi-Fi Gaming Network Participation',
    #         'def': 'Binary flag—student devices connected to high-traffic gaming ports for ≥ 5 hours/week during evenings.',
    #         'feedback': {
    #             'include': 'Correlation to retention unproven; risk of pathologising hobby behaviour. Provide theoretical justification or exclude.',
    #             'exclude': 'Sensible—no established link to academic persistence.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_wi_fi_choice(),
    #         'textbox': wi_fi_textbox,
    #         'buttons': {
    #             'include': wi_fi_incl,
    #             'exclude': wi_fi_excl,
    #             'other': wi_fi_flag,
    #         },
    #     },
    # }
    return


@app.cell(hide_code=True)
def task_4_selection(
    continue_to_task_4,
    mo,
    variable_selection_output,
    variables_by_task,
):
    mo.stop(not continue_to_task_4())

    task_4_display_output = [variable_selection_output(var) for var in variables_by_task[4]['variables']]

    mo.output.replace(
        mo.vstack(task_4_display_output)
    )
    return


@app.cell(hide_code=True)
def task_4_detailed_feedback(
    continue_to_task_4,
    generate_feedback,
    mo,
    variables_by_task,
):
    mo.stop(not continue_to_task_4())

    task_4_feedback = [generate_feedback(var) for var in variables_by_task[4]['variables']]

    task_4_content_detail_feedback = mo.vstack(task_4_feedback)

    mo.accordion({"Detailed Feedback": task_4_content_detail_feedback})
    return


@app.cell(hide_code=True)
def section_separator(continue_to_task_4, mo):
    mo.stop(not continue_to_task_4())

    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell
def wrapup_intro(mo, reactive_dict):
    # ---- Global submit state ----
    submit_state, set_submit_state = mo.state(False)

    # ---- Collect all choices ----
    # variable_detailsa = [task_1_variable_details, task_2_variable_details, task_3_variable_details, task_4_variable_details]
    all_choices = [reactive_dict[var]['getter'] for var in reactive_dict]

    # ---- Count included variables ----
    include_count = sum(1 for c in all_choices if c == 'include')

    # ---- Keep returning states for later use ----
    return (include_count,)


@app.cell(hide_code=True)
def wrapup_summary_table(
    continue_to_final_check,
    decision_label,
    include_count,
    mo,
    reactive_dict,
    variable_details,
    variables_by_task,
):
    mo.stop(not continue_to_final_check())

    variable_plural = "variable" if include_count == 1 else "variables"

    grouped_rows = {
        variables_by_task[task]['header']: [
            (decision_label(reactive_dict[var]['getter']), 
             variable_details[var]['title']) 
            for var in variables_by_task[task]['variables']
        ]
        for task in variables_by_task
    }

    # build table HTML
    table_html = "<table style='border-collapse:collapse; width:100%; text-align:left;'>"
    table_html += "<thead><tr><th>Group (Wave)</th><th>Decision</th><th>Variable</th></tr></thead><tbody>"

    for group, rows in grouped_rows.items():
        # group header row
        table_html += f"<tr><td colspan='3' style='font-weight:bold; padding-top:10px;'>{group}</td></tr>"
        # variable rows
        for decision, variable in rows:
            color = " style='background-color:#e8f5e9;'" if decision == "Include" else ""
            table_html += f"<tr{color}><td></td><td>{decision}</td><td>{variable}</td></tr>"
        # blank line between groups
        table_html += "<tr><td colspan='3' style='height:8px;'></td></tr>"

    table_html += "</tbody></table>"

    mo.vstack([
        mo.md("## End-of-Scenario Wrap-Up – Variable-Selection Brief"),
        mo.md(
        f"**_Your model will use the {include_count} {variable_plural} highlighted in green._** "
        "Is this acceptable, or would you like to revise your selections?"
    ),
        mo.Html(table_html)
    ])
    return


@app.cell(hide_code=True)
def review_wave_buttons(continue_to_final_check, mo):
    mo.stop(not continue_to_final_check())

    button_output = []
    for num in range(1, 5):
        temp_md = f"""<a href=#task_{num}>""""""{temp_button}</a>"""
        temp_label = f"""Review Wave {num}"""
        button_output.append(mo.md(temp_md).batch(temp_button=mo.ui.button(label=temp_label)))
    mo.hstack(
        button_output
    )
    return


@app.cell
def _(continue_to_final_check, mo):
    mo.stop(not continue_to_final_check())
    mo.Html(f"""<hr style="border: 3px solid #4CAF50; margin-top:1rem; margin-bottom:1rem;">""")
    return


@app.cell
def _(
    continue_to_final_feedback,
    format_final_feedback,
    gather_final_feedback,
    mo,
    variables_by_task,
):
    mo.stop(not continue_to_final_feedback())

    final_feedback_header = mo.Html(f"""<div style="text-align:center; color:#4CAF50; font-size:1.5rem; font-weight:bold; margin-bottom:1rem;">Final Feedback </div>""")

    final_output = []

    for task in variables_by_task: 
        local_header = f"""{variables_by_task[task]['header']} Feedback"""
        cor = []
        incor = []
        for var in variables_by_task[task]['variables']: 
            cor, incor = gather_final_feedback(var, cor, incor)
        final_task_output = format_final_feedback(cor, incor)
        final_output.append(mo.accordion({local_header: final_task_output}))

    mo.vstack([final_feedback_header]+ final_output)
    return


@app.cell
def task_f(continue_to_final_feedback, mo):
    mo.stop(not continue_to_final_feedback())

    product_textbox = mo.ui.text_area(label="Enter your product notes here", rows=8)
    learner_reflection_textbox = mo.ui.text_area(label="Please wriet your reflections here", rows=12)

    mo.vstack([
        mo.md("## Placeholder for Product"),
        mo.Html("<div style='width:100%;'>"),  # force full-width container
        product_textbox,
        mo.Html("</div>"),

        mo.md("&nbsp;"),

        mo.md("## Placeholder for Learner Reflection"),
        mo.Html("<div style='width:100%;'>"),
        learner_reflection_textbox,
        mo.Html("</div>"),
        mo.md("&nbsp;"),
    ])
    return


@app.cell(hide_code=True)
def _():
    # for numba in list(vardict.keys())[2:]: 
    #     for item in vardict[numba]: 
    #         print(f"""\t{item.name}: """+'{\n'+f"""\t\t'state': set_{item.name}_state,\n\t\t'initial': set_{item.name}_initial,\n\t\t'final': set_{item.name}_final,\n"""+'\t},')
    return


@app.cell(hide_code=True)
def task_1_selections():
    # task_1_display_output = [variable_selection_output(var) for var in variables_by_task[1]['variables']]

    # mo.output.replace(
    #     mo.vstack(task_1_display_output)
    # )
    return


@app.cell(hide_code=True)
def task_1_detailed_feedback():
    # task_1_feedback = [generate_feedback(var) for var in variables_by_task[1]['variables']]

    # content_detail_feedback = mo.vstack(task_1_feedback)

    # mo.accordion({"Detailed Feedback": content_detail_feedback})
    return


@app.cell(hide_code=True)
def _():




    # #task 1 buttons
    # #pell
    # pell_incl = mo.ui.run_button(label="Include", kind='success',
    #                              on_change=lambda _: set_pell_state('include'))
    # pell_excl = mo.ui.run_button(label="Exclude", kind='danger',
    #                              on_change=lambda _: set_pell_state('exclude'))
    # pell_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
    #                              on_change=lambda _: set_pell_state('flag'))


    # #efc
    # efc_incl = mo.ui.run_button(label="Include", kind='success', 
    #                             on_change=lambda _: set_efc_state("include"))
    # efc_excl = mo.ui.run_button(label="Exclude", kind='danger', 
    #                             on_change=lambda _: set_efc_state("exclude"))
    # efc_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
    #                             on_change=lambda _: set_efc_state("flag"))

    # #sai
    # sai_incl = mo.ui.run_button(label="Include", kind='success', 
    #                             on_change=lambda _: set_sai_state("include"))
    # sai_excl = mo.ui.run_button(label="Exclude", kind='danger', 
    #                             on_change=lambda _: set_sai_state("exclude"))
    # sai_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
    #                             on_change=lambda _: set_sai_state("flag"))

    # #unmet_need
    # unmet_incl = mo.ui.run_button(label="Include", kind='success', 
    #                               on_change=lambda _: set_unmet_state("include"))
    # unmet_excl = mo.ui.run_button(label="Exclude", kind='danger', 
    #                               on_change=lambda _: set_unmet_state("exclude"))
    # unmet_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
    #                               on_change=lambda _: set_unmet_state("flag"))

    # #merit_award_amount
    # merit_incl = mo.ui.run_button(label="Include", kind='success',
    #                               on_change=lambda _: set_merit_state("include"))
    # merit_excl = mo.ui.run_button(label="Exclude", kind='danger', 
    #                               on_change=lambda _: set_merit_state("exclude"))
    # merit_flag = mo.ui.run_button(label="Flag for Review", kind='warn',
    #                               on_change=lambda _: set_merit_state('flag'))


    # #pell_plus
    # pell_plus_incl = mo.ui.run_button(label="Include", kind='success',
    #                                   on_change=lambda _: set_pell_plus_state("include"))
    # pell_plus_excl = mo.ui.run_button(label="Exclude", kind='danger',
    #                                   on_change=lambda _: set_pell_plus_state("exclude"))
    # pell_plus_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
    #                                   on_change=lambda _: set_pell_plus_state('flag'))


    # #text areas
    # pell_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Pell Grant selection", rows=4)
    # efc_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} EFC selection", rows=4)
    # sai_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} SAI selection", rows=4)
    # unmet_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Unmet Need selection", rows=4)
    # merit_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Merit Award selection", rows=4)
    # pell_plus_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Pell Plus selection", rows=4)




    # #buttons
    # #button_labels

    # #race
    # race_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_race_choice('include'))
    # race_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_race_choice('audit'))
    # race_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_race_choice('exclude'))

    # #gender
    # gender_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_gender_choice('include'))
    # gender_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_gender_choice('audit'))
    # gender_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_gender_choice('exclude'))

    # #age
    # age_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_age_choice('include'))
    # age_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_age_choice('audit'))
    # age_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_age_choice('exclude'))

    # #pronouns
    # pronoun_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_pronoun_choice('include'))
    # pronoun_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_pronoun_choice('audit'))
    # pronoun_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_pronoun_choice('exclude'))

    # #textboxes
    # race_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Race selection", rows=4)
    # gender_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Gender selection", rows=4)
    # age_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Age selection", rows=4)
    # pronoun_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Preferred Pronouns selection", rows=4)




    # #buttons

    # #labels

    # #gpa
    # gpa_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_gpa_choice('include'))
    # gpa_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_gpa_choice('exclude'))
    # gpa_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_gpa_choice('flag_impr'))

    # #test_scores
    # scores_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_scores_choice('include'))
    # scores_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_scores_choice('exclude'))
    # scores_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_scores_choice('flag_impr'))


    # #midterm grades
    # midterms_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_midterms_choice('include'))
    # midterms_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_midterms_choice('exclude'))
    # midterms_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_midterms_choice('flag_impr'))

    # #epr
    # epr_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_epr_choice('include'))
    # epr_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_epr_choice('exclude'))
    # epr_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_epr_choice('flag_impr'))

    # #printer
    # printer_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_printer_choice('include'))
    # printer_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_printer_choice('exclude'))
    # printer_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_printer_choice('flag_impr'))

    # #textboxes
    # gpa_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} High School GPA selection.")
    # scores_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Test Scores selection.")
    # midterms_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Midterm Grades selection.")
    # epr_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Early Progress Reports selection.")
    # printer_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Dorm Printer Usage selection.")



    # #buttons
    # #labels 

    # #legacy_status
    # legacy_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_legacy_choice('include'))
    # legacy_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_legacy_choice('exclude'))
    # legacy_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_legacy_choice('flag_impr'))

    # #student_athlete_status
    # athlete_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_athlete_choice('include'))
    # athlete_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_athlete_choice('exclude'))
    # athlete_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_athlete_choice('flag_impr'))

    # #first_generation_student
    # firstgen_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_firstgen_choice('include'))
    # firstgen_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_firstgen_choice('exclude'))
    # firstgen_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_firstgen_choice('flag_impr'))

    # #distance_from_home
    # distance_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_distance_choice('include'))
    # distance_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_distance_choice('exclude'))
    # distance_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_distance_choice('flag_impr'))

    # #credits_after_add_drop
    # credits_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_credits_choice('include'))
    # credits_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_credits_choice('exclude'))
    # credits_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_credits_choice('flag_impr'))

    # #live_on_campus_or_commute
    # housing_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_housing_choice('include'))
    # housing_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_housing_choice('exclude'))
    # housing_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_housing_choice('flag_impr'))

    # #residency_in_state_out_of_state_international
    # residency_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_residency_choice('include'))
    # residency_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_residency_choice('exclude'))
    # residency_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_residency_choice('flag_impr'))

    # #urban_rural_suburban_origin
    # origins_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_origins_choice('include'))
    # origins_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_origins_choice('exclude'))
    # origins_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_origins_choice('flag_impr'))

    # #transfer_status
    # transfer_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_transfer_choice('include'))
    # transfer_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_transfer_choice('exclude'))
    # transfer_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_transfer_choice('flag_impr'))

    # #extracurricular_involvement
    # extracurricular_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', 
    #                                         on_change=lambda _: set_extracurricular_choice('include'))
    # extracurricular_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', 
    #                                         on_change=lambda _: set_extracurricular_choice('exclude'))
    # extracurricular_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', 
    #                                         on_change=lambda _: set_extracurricular_choice('flag_impr'))

    # #campus_wi_fi_gaming_network_participation
    # wi_fi_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_wi_fi_choice('include'))
    # wi_fi_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_wi_fi_choice('exclude'))
    # wi_fi_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_wi_fi_choice('flag_impr'))


    # #textboxes
    # legacy_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Legacy Status selection.")
    # athlete_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Student Athlete Status selection.")
    # firstgen_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} First-Generation Status selection.")
    # distance_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Distance From Home selection.")
    # credits_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Credits After Add/Drop selection.")
    # housing_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Living On Campus or Commuter selection.")
    # residency_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Residency (In-State / Out-of-State / International) selection.")
    # origins_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Urban / Rural / Suburban Origin selection")
    # transfer_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Transfer Status selection.")
    # extracurricular_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Extracurricular Involvement selection.")
    # wi_fi_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Campus Wi-Fi Gaming Network Participation selection.")


    # task_2_labels = {'include': 'Include As-Is', 'exclude': 'Exclude Entirely', 'audit': 'Keep for Bias-Audit Only'}
    # task_3_labels = {'include': 'Include as-is', 'exclude': 'Exclude (too unreliable)', 'flag_impr': 'Flag for Data-Quality Improvement'}
    # task_4_labels = {'include': 'Include as-is', 'exclude': 'Exclude (too unreliable)', 'other': 'Flag for Data-Quality Improvement'}
    return


@app.cell(hide_code=True)
def reactive_dictionary():
    # reactive_dict = {
    #     'pell': {
    #         'include': pell_incl,
    #         'exclude': pell_excl,
    #         'other': pell_flag,
    #         'textbox': pell_textbox,
    #         'getter': get_pell_state(),
    #         'setter': set_pell_state
    #     }, 
    #     'efc': {
    #         'include': efc_incl,
    #         'exclude': efc_excl,
    #         'other': efc_flag,
    #         'textbox': efc_textbox,
    #         'getter': get_efc_state(),
    #     },
    #     'sai': {
    #         'include': sai_incl,
    #         'exclude': sai_excl,
    #         'other': sai_flag,
    #         'textbox': sai_textbox,
    #         'getter': get_sai_state(),
    #     },
    #     'unmet': {
    #         'include': unmet_incl,
    #         'exclude': unmet_excl,
    #         'other': unmet_flag,
    #         'textbox': unmet_textbox,
    #         'getter': get_unmet_state(),
    #     },
    #     'merit': {
    #         'include': merit_incl,
    #         'exclude': merit_excl,
    #         'other': merit_flag,
    #         'textbox': merit_textbox,
    #         'getter': get_merit_state(),
    #     },
    #     'pell_plus': {
    #         'include': pell_plus_incl,
    #         'exclude': pell_plus_excl,
    #         'other': pell_plus_flag,
    #         'textbox': pell_plus_textbox,
    #         'getter': get_pell_plus_state(),
    #     },
    #     'race': {
    #         'include': race_incl,
    #         'exclude': race_excl,
    #         'other': race_audit,
    #         'textbox': race_textbox,
    #         'getter': get_race_choice(),
    #     }, 
    #     'gender': {
    #         'include': gender_incl,
    #         'exclude': gender_excl,
    #         'other': gender_audit,
    #         'textbox': gender_textbox,
    #         'getter': get_gender_choice(),
    
    #     },
    #     'age': {
    #         'include': age_incl,
    #         'exclude': age_excl,
    #         'other': age_audit,
    #         'textbox': age_textbox,
    #         'getter': get_age_choice(),
        
    #     },
    #     'pronouns': {
    #         'include': pronoun_incl,
    #         'exclude': pronoun_excl,
    #         'other': pronoun_audit,
    #         'textbox': pronoun_textbox,
    #         'getter': get_pronoun_choice(),      
    #     },
    #     "gpa": {
    #         'include': gpa_incl,
    #         'exclude': gpa_excl,
    #         'other': gpa_flag,
    #         'textbox': gpa_textbox,
    #         'getter': get_gpa_choice(),

    #     },
    #     "scores": {
    #         'include': scores_incl,
    #         'exclude': scores_excl,
    #         'other': scores_flag,
    #         'textbox': scores_textbox,
    #         'getter': get_scores_choice(),
        
    #     },
    #     "midterms": {
    #         'include': midterms_incl,
    #         'exclude': midterms_excl,
    #         'other': midterms_flag,
    #         'textbox': midterms_textbox,
    #         'getter': get_midterms_choice(),
        
    #     },
    #     "epr": {
    #         'include': epr_incl,
    #         'exclude': epr_excl,
    #         'other': epr_flag,
    #         'textbox': epr_textbox,
    #         'getter': get_epr_choice(),
        
    #     },
    #     "printer": {
    #         'include': printer_incl,
    #         'exclude': printer_excl,
    #         'other': printer_flag,
    #         'textbox': printer_textbox,
    #         'getter': get_printer_choice(),        
    #     },
    #     'legacy': {
    #         'include': legacy_incl,
    #         'exclude': legacy_excl,
    #         'other': legacy_flag,
    #         'textbox': legacy_textbox,
    #         'getter': get_legacy_choice(),
    #     }, 
    #     'athlete': {
    #         'include': athlete_incl,
    #         'exclude': athlete_excl,
    #         'other': athlete_flag,
    #         'textbox': athlete_textbox,
    #         'getter': get_athlete_choice(),
    #     }, 
    #     'firstgen': {
    #         'include': firstgen_incl,
    #         'exclude': firstgen_excl,
    #         'other': firstgen_flag,
    #         'textbox': firstgen_textbox,
    #         'getter': get_firstgen_choice(),
    #     }, 
    #     'distance': {
    #         'include': distance_incl,
    #         'exclude': distance_excl,
    #         'other': distance_flag,
    #         'textbox': distance_textbox,
    #         'getter': get_distance_choice(),
    #     }, 
    #     'credits': {
    #         'include': credits_incl,
    #         'exclude': credits_excl,
    #         'other': credits_flag,
    #         'textbox': credits_textbox,
    #         'getter': get_credits_choice(),
    #     }, 
    #     'housing': {
    #         'include': housing_incl,
    #         'exclude': housing_excl,
    #         'other': housing_flag,
    #         'textbox': housing_textbox,
    #         'getter': get_housing_choice(),
    #     }, 
    #     'residency': {
    #         'include': residency_incl,
    #         'exclude': residency_excl,
    #         'other': residency_flag,
    #         'textbox': residency_textbox,
    #         'getter': get_residency_choice(),
    #     }, 
    #     'origins': {
    #         'include': origins_incl,
    #         'exclude': origins_excl,
    #         'other': origins_flag,
    #         'textbox': origins_textbox,
    #         'getter': get_origins_choice(),
    #     }, 
    #     'transfer': {
    #         'include': transfer_incl,
    #         'exclude': transfer_excl,
    #         'other': transfer_flag,
    #         'textbox': transfer_textbox,
    #         'getter': get_transfer_choice(),
    #     }, 
    #     'extracurricular': {
    #         'include': extracurricular_incl,
    #         'exclude': extracurricular_excl,
    #         'other': extracurricular_flag,
    #         'textbox': extracurricular_textbox,
    #         'getter': get_extracurricular_choice(),
    #     },
    #     'wi_fi': {
    #         'include': wi_fi_incl,
    #         'exclude': wi_fi_excl,
    #         'other': wi_fi_flag,
    #         'textbox': wi_fi_textbox,
    #         'getter': get_wi_fi_choice(),
    #     },
    # }
    return


if __name__ == "__main__":
    app.run()
