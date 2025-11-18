import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo                           
    mo.md(
        "# Variable selection scenario\n"

    )
    return (mo,)


@app.cell
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
def rsdo_functions():

    # #functions
    # def var_selection_text_generator(choice:str)->str: 
    #     if choice == 'include': 
    #         insert_text = "🟢 **Include** the variable **as-is**."
    #     if choice == 'exclude':
    #         insert_text = "🔴 **Exclude** the variable **entirely**."
    #     if choice == 'flag': 
    #         insert_text = "🟡 **Flag** the variable **for Review**."
    #     if choice == 'audit': 
    #         insert_text = '🟠 **Keep** the variable **for Bias-Audit Only**.'
    #     if choice == 'flag_impr': 
    #         insert_text = '🟠 **Flag** the variable **for Data-Quality Improvement**.'
    #     if choice == 'exclude_unre': 
    #         insert_text == "🔴 **Exclude** the variable **due to unreliability**."
    #     if not choice:
    #         insert_text = "⚪️ **not yet selected**"
    #         return f"You have {insert_text} a variable option."
    #     return f"You decided to {insert_text}"


    # def generate_detailed_feedback_text(variable_details): 
    #     title = variable_details['background']['title']
    #     getter = variable_details['reactive_elements']['getter']
    #     message = variable_details['feedback']['initial'][getter] if getter else ''
    #     return f"""**{title}:** {message}"""


    # def variable_selection_output(variable_details): 
    #     buttons = variable_details['reactive_elements']['buttons']
    #     title = variable_details['background']['title']
    #     definition = variable_details['background']['def']
    #     getter = variable_details['reactive_elements']['getter']
    #     textbox = variable_details['reactive_elements']['textbox']
    #     content = mo.vstack([
    #         mo.md(definition),
    #         mo.hstack([buttons['include'], buttons['exclude'], buttons['other']], gap='1rem')
    #     ])
    #     output = mo.vstack([
    #         mo.accordion({title: content}),
    #         mo.md(f"""{var_selection_text_generator(getter)}"""),
    #         textbox if getter else ''
    #     ])
    #     return output

    # def variable_selection_output_2(variable_details): 
    #     buttons = variable_details['reactivity']['buttons']
    #     title = variable_details['title']
    #     definition = variable_details['def']
    #     getter = variable_details['reactivity']['getter']
    #     textbox = variable_details['reactivity']['textbox']
    #     content = mo.vstack([
    #         mo.md(definition),
    #         mo.hstack([buttons['include'], buttons['exclude'], buttons['other']], gap='1rem')
    #     ])
    #     output = mo.vstack([
    #         mo.accordion({title: content}),
    #         mo.md(f"""{var_selection_text_generator(getter)}"""),
    #         textbox if getter else ''
    #     ])
    #     return output


    # def generate_feedback(variable_options: dict[str|dict, str]):
    #     choice = variable_options['reactive_elements']['getter']
    #     if choice: 
    #         if choice in variable_options['feedback']['initial']:
    #             feedback_message = variable_options['feedback']['initial'][choice]
    #         else: 
    #             feedback_message = variable_options['feedback']['initial']['other']
    #     else: 
    #         feedback_message = ''
    #     return mo.md(f"""**{variable_options['background']['title']}:** {feedback_message}""")


    # def generate_feedback_2(variable_options): 
    #     choice = variable_options['reactivity']['getter']
    #     feedback_message = variable_options['feedback'][choice] if choice else ''
    #     return mo.md(f"""**{variable_options['title']}:** {feedback_message}""")


    # def decision_label(choice):
    #     if choice in ["include", "include_as_is", "include_as-is"]:
    #         return "Include"
    #     elif choice in ["flag", "flag_improvement", "audit_only"]:
    #         return "Flag"
    #     elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
    #         return "Exclude"
    #     else:
    #         return "No Selection"


    # def gather_final_feedback(variable_settings, correct_list, incorrect):
    #     title = variable_settings['background']['title']
    #     choice = variable_settings['reactive_elements']['getter']
    #     if choice: 
    #         if choice not in ['include', 'exclude']: 
    #             choice = 'other'
    #         feedback = variable_settings['feedback']['final'][choice] 
    #         if feedback == correct:
    #             correct_list.append(title)
    #         else: 
    #             incorrect.append(mo.md(f"""**{title}**: {feedback}"""))
    #     else: 
    #         incorrect.append(mo.md(f"""**{title}**: No variable was selected."""))
    #     return correct_list, incorrect


    # def format_final_feedback(correct, incorrect): 
    #     corr_text = f"""✅ **No major concerns for:** {', '.join(correct)}""" if len(correct)>0 else ""
    #     corr_output = mo.md(corr_text)
    #     incorr_text = "⚠️ **At least one restricted variable still needs your attention.**" if len(incorrect)>0 else "✅ **Everything looks good in this wave!**"
    #     incorr_output = mo.md(incorr_text)
    #     final_output = mo.vstack([incorr_output] + incorrect + [corr_output])
    #     return final_output
    return


@app.cell
def _():
    #constants_1
    textbox_text_boilerplate = 'Please briefly justify your reasoning for your'
    correct = "Right Choice"
    return correct, textbox_text_boilerplate


@app.cell
def _(
    task_1_variable_details,
    task_2_variable_details,
    task_3_variable_details,
    task_4_variable_details,
):
    #constants

    task_heading_to_task_data = {
        'Regulatory Gate Feedback': task_1_variable_details,
        'Protected-Attribute Gate Feedback': task_2_variable_details,
        'Data-Reliability Gate Feedback': task_3_variable_details,
        'Equity & Actionability Gate Feedback': task_4_variable_details,
    }
    return (task_heading_to_task_data,)


@app.cell
def _():
    return


@app.cell
def _(VariableGenerator):


    efc = VariableGenerator(var_name='efc',
                            title = 'Expected Family Contribution (EFC)',
                            definition = "Amount a family is expected to contribute to education costs (legacy FAFSA metric). "
                            "Regulatory compliance requires excluding this sensitive financial information.",
                            task=1,
                            order=2,
                           )
    efc.add_to_set()
    sai = VariableGenerator(var_name='sai',
                            title="Student Aid Index (SAI)",
                            definition="A new metric from recent FAFSA changes that replaced EFC. "
                            "Recent implementation means this data may not be available for all students in your historical dataset.",
                            task=1,
                            order=3,
                           )
    unmet = VariableGenerator(var_name='unmet',
                              title="Unmet Need",
                              definition="Gap between the cost of attendance and the student’s available resources. "
                              "Financial-stress indicator, but regulatory restrictions likely prohibit its use in "
                              "individual-level models.",
                              task=1,
                              order=4,
                             )
    merit = VariableGenerator(var_name='merit',
                              title="Merit Award Amount",
                              definition="Scholarship amounts awarded based on academic achievement rather than financial need. "
                              "Consider whether this variable primarily reflects prior achievement or introduces "
                              "socioeconomic factors into your model.",            
                              task=1,
                              order=5,
                             )
    pell_plus = VariableGenerator(var_name='pell_plus',
                                  title="Pell Plus",
                                  definition="University matching funds that complement federal Pell Grants. "
                                  "Financial-aid variables like this are likely subject to the same regulatory restrictions "
                                  "as other financial data.",
                                  task=1,
                                  order=6,
                                 )
    return efc, merit, pell_plus, sai, unmet


@app.cell
def _(correct):
    task_1_label = 'Flag for Review'
    task_1_return = 'flag'

    feedback = {
        'pell': {
            'initial': {
                    'include': 'Including Pell Status violates current federal guidance and may expose the institution to penalties.'
                               'Consider aggregate reporting instead of individual-level use.',
                    'exclude': correct,
                    'flag': 'Flagged',
                },
            'final': {
                'include': "Including Pell Status violates current federal guidance and may expose the institution to penalties. "
                           "Consider aggregate reporting instead of individual-level use.",
                'exclude': correct,
                'flag': correct,
            } 
        },
        'efc': {
            'initial': {
                    'include': 'EFC is explicitly barred under 2024 Department of Education rules; '
                               'its inclusion would render the model non-compliant.',
                    'exclude': correct, 
                    'flag': 'Flagged',
                },
            'final': {
                'include': "EFC is explicitly barred under 2024 Department of Education rules; "
                           "its inclusion would render the model non-compliant.",
                'exclude': correct,
                'flag': correct,
            },
        },
        'sai': {
            'initial': {
                    'include': 'SAI is sensitive financial-aid data with incomplete coverage. Using it risks privacy '
                               'violations and injects missing-data bias.',
                    'exclude': correct,
                    'flag': 'Flagged',
                },
            'final': {
                'include': "SAI is sensitive financial-aid data with incomplete coverage. "
                           "Using it risks privacy violations and injects missing-data bias.",
                'exclude': correct,
                'flag': correct,                
            },        
        },
        'unmet': {
            'initial': {
                    'include': 'Unmet Need combines multiple restricted data points. '
                               'Including it would contravene policy and amplify socioeconomic bias.',
                    'exclude': correct,
                    'flag': 'Flagged',
                },
            'final': {
                'include': "Unmet Need combines multiple restricted data points. "
                           "Including it would contravene policy and amplify socioeconomic bias.",
                'exclude': correct,
                'flag': correct,
            },
        },
        'merit': {
            'initial': {
                    'include': 'Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. '
                               'Use only with a strong equity justification.',
                    'exclude': correct,
                    'flag': 'Flagged',
                },
            'final': {
                'include': "Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. "
                           "Use only with a strong equity justification.",
                'exclude': correct,
                'flag': correct,
            },
        },
        'pell_plus': {
            'initial': {
                    'include': 'Pell Plus directly signals Pell participation; individual-level use is restricted. '
                               'Exclude or seek explicit legal clearance.',
                    'exclude': correct,
                    'flag': 'Flagged',
                },
            'final': {
                'include': "Pell Plus directly signals Pell participation; individual-level use is restricted. "
                           "Exclude or seek explicit legal clearance.",
                'exclude': correct,
                'flag': correct,
            },
        }
    }
    return


@app.cell
def _(
    efc_excl,
    efc_flag,
    efc_incl,
    efc_textbox,
    get_pell_state,
    merit_excl,
    merit_flag,
    merit_incl,
    merit_textbox,
    pell_excl,
    pell_flag,
    pell_incl,
    pell_plus_excl,
    pell_plus_flag,
    pell_plus_incl,
    pell_plus_textbox,
    pell_textbox,
    sai_excl,
    sai_flag,
    sai_incl,
    sai_textbox,
    set_pell_state,
    unmet_excl,
    unmet_flag,
    unmet_incl,
    unmet_textbox,
):
    reactive_dict = {
        'pell': {
            'include': pell_incl,
            'exclude': pell_excl,
            'other': pell_flag,
            'textbox': pell_textbox,
            'getter': get_pell_state(),
            'setter': set_pell_state
        }, 
        'efc': {
            'include': efc_incl,
            'exclude': efc_excl,
            'other': efc_flag,
            'textbox': efc_textbox,
        },
        'sai': {
            'include': sai_incl,
            'exclude': sai_excl,
            'other': sai_flag,
            'textbox': sai_textbox,
        },
        'unmet': {
            'include': unmet_incl,
            'exclude': unmet_excl,
            'other': unmet_flag,
            'textbox': unmet_textbox,
        },
        'merit': {
            'include': merit_incl,
            'exclude': merit_excl,
            'other': merit_flag,
            'textbox': merit_textbox,
        },
        'pell_plus': {
            'include': pell_plus_incl,
            'exclude': pell_plus_excl,
            'other': pell_plus_flag,
            'textbox': pell_plus_textbox,
        }
    }
    return (reactive_dict,)


@app.cell
def task_1_elements_and_states(
    efc,
    merit,
    mo,
    pell,
    pell_plus,
    sai,
    textbox_text_boilerplate,
    unmet,
):
    #task 1 getters and setters
    get_pell_state, set_pell_state = mo.state(None)
    get_efc_state, set_efc_state = mo.state(None)
    get_sai_state, set_sai_state = mo.state(None)
    get_unmet_state, set_unmet_state = mo.state(None)
    get_merit_state, set_merit_state = mo.state(None)
    get_pell_plus_state, set_pell_plus_state = mo.state(None)


    def change_feedback(obj, setter, status): 
        setter(status)
        obj.set_feedback(status)
        obj.getter()




    #task 1 buttons
    #pell
    pell_incl = mo.ui.run_button(label="Include", kind='success',
                                 on_change=lambda _: change_feedback(pell, set_pell_state, 'include'))
    pell_excl = mo.ui.run_button(label="Exclude", kind='danger',
                                 on_change=lambda _: change_feedback(pell, set_pell_state, 'exclude'))
    pell_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
                                 on_change=lambda _: change_feedback(pell, set_pell_state, 'flag'))


    #efc
    efc_incl = mo.ui.run_button(label="Include", kind='success', 
                                on_change=lambda _: change_feedback(efc, set_efc_state, "include"))
    efc_excl = mo.ui.run_button(label="Exclude", kind='danger', 
                                on_change=lambda _: change_feedback(efc, set_efc_state, "exclude"))
    efc_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
                                on_change=lambda _: change_feedback(efc, set_efc_state, "flag"))
    efc.incl = efc_incl
    efc.excl = efc_excl
    efc.other = efc_flag
    efc.getter = get_efc_state

    #sai
    sai_incl = mo.ui.run_button(label="Include", kind='success', 
                                on_change=lambda _: change_feedback(sai, set_sai_state, "include"))
    sai_excl = mo.ui.run_button(label="Exclude", kind='danger', 
                                on_change=lambda _: change_feedback(sai, set_sai_state, "exclude"))
    sai_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
                                on_change=lambda _: change_feedback(sai, set_sai_state, "flag"))
    sai.incl = sai_incl
    sai.excl = sai_excl
    sai.other = sai_flag
    sai.getter = get_sai_state



    #unmet_need
    unmet_incl = mo.ui.run_button(label="Include", kind='success', 
                                  on_change=lambda _: change_feedback(unmet, set_merit_state, "include"))
    unmet_excl = mo.ui.run_button(label="Exclude", kind='danger', 
                                  on_change=lambda _: change_feedback(unmet, set_merit_state, "exclude"))
    unmet_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
                                  on_change=lambda _: change_feedback(unmet, set_merit_state, "flag"))
    unmet.incl = unmet_incl
    unmet.excl = unmet_excl
    unmet.other = unmet_flag
    unmet.getter = get_unmet_state



    #merit_award_amount
    merit_incl = mo.ui.run_button(label="Include", kind='success',
                                  on_change=lambda _: change_feedback(merit, set_merit_state, "include"))
    merit_excl = mo.ui.run_button(label="Exclude", kind='danger', 
                                  on_change=lambda _: change_feedback(merit, set_merit_state, "exclude"))
    merit_flag = mo.ui.run_button(label="Flag for Review", kind='warn',
                                  on_change=lambda _: change_feedback(merit, set_merit_state, 'flag'))
    merit.incl = merit_incl
    merit.excl = merit_excl
    merit.other = merit_flag
    merit.getter =get_merit_state


    #pell_plus
    pell_plus_incl = mo.ui.run_button(label="Include", kind='success',
                                      on_change=lambda _: change_feedback(pell_plus, set_pell_plus_state, "include"))
    pell_plus_excl = mo.ui.run_button(label="Exclude", kind='danger',
                                      on_change=lambda _: change_feedback(pell_plus, set_pell_plus_state, "exclude"))
    pell_plus_flag = mo.ui.run_button(label="Flag for Review", kind='warn', 
                                      on_change=lambda _: change_feedback(pell_plus, set_pell_plus_state, 'flag'))
    pell_plus.incl = pell_plus_incl
    pell_plus.excl = pell_plus_excl
    pell_plus.other = pell_plus_flag
    pell_plus.getter = get_pell_plus_state


    #text areas
    pell_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Pell Grant selection", rows=4)
    efc_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} EFC selection", rows=4)
    sai_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} SAI selection", rows=4)
    unmet_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Unmet Need selection", rows=4)
    merit_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Merit Award selection", rows=4)
    pell_plus_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Pell Plus selection", rows=4)
    pell_plus.textbox = pell_plus_textbox
    return (
        efc_excl,
        efc_flag,
        efc_incl,
        efc_textbox,
        get_pell_state,
        merit_excl,
        merit_flag,
        merit_incl,
        merit_textbox,
        pell_excl,
        pell_flag,
        pell_incl,
        pell_plus_excl,
        pell_plus_flag,
        pell_plus_incl,
        pell_plus_textbox,
        pell_textbox,
        sai_excl,
        sai_flag,
        sai_incl,
        sai_textbox,
        set_pell_state,
        unmet_excl,
        unmet_flag,
        unmet_incl,
        unmet_textbox,
    )


@app.cell
def _(get_pell_state, pell):
    pell.var_name='pell'
    pell.title='Pell Status'
    pell.definition="Whether a student receives a federal Pell Grant. New regulations restrict use of financial-aid data in predictive modeling."
    pell.order=1
    pell.getter = get_pell_state
    return


@app.cell
def _(mo, variable_selection_output, variable_set):
    task_1_display_output3 = [variable_selection_output(item) for item in variable_set]

    mo.output.replace(
        mo.vstack(task_1_display_output3)
    )
    return


@app.cell
def _(efc):
    efc.initial_feedback
    return


@app.cell
def _(efc):
    efc.feedback
    return


@app.cell
def _(mo, pell, variable_selection_output):
    task_1_display_output2 = [variable_selection_output(item) for item in [pell]]

    mo.output.replace(
        mo.vstack(task_1_display_output2)
    )
    return


@app.cell
def _():
    # content = mo.vstack([
    #     mo.md(pell.definition),
    #     mo.hstack([pell.incl, pell.excl, pell.other], gap='1rem')
    # ])
    # output = mo.vstack([
    #     mo.accordion({pell.title: content}),
    #     mo.md(f"""{var_selection_text_generator(get_pell_state())}"""),
    #     pell_textbox if get_pell_state() else ''
    # ])
    # mo.output.replace(output)
    return


@app.cell
def _():
    # #task 1 getters and setters
    # get_pell_state, set_pell_state = mo.state(None)
    # get_efc_state, set_efc_state = mo.state(None)
    # get_sai_state, set_sai_state = mo.state(None)
    # get_unmet_state, set_unmet_state = mo.state(None)
    # get_merit_state, set_merit_state = mo.state(None)
    # get_pell_plus_state, set_pell_plus_state = mo.state(None)

    # thing2 = []

    def change_the_thing(obj, text): 
        obj.setter(text)
        obj.getter1()
        obj.rename_var(text)


    # class VariableGenerator: 
    #     def __init__(self, variable_name=None, variable_dict=None, title=None, definition=None, incl=None, excl=None, other=None, text=None, getter=None, setter=None):
    #         self.title = title
    #         textbox_label = f"""{textbox_text_boilerplate} {self.title} selection"""
    #         self.name = variable_name
    #         self.definition = definition
    #         self.initial_feedback = None
    #         self.final_feedback = None
    #         thing2.append(self)
    #         self.incl = incl
    #         self.excl = excl
    #         self.other = other
    #         self.text = text
    #         self.getter = getter
    #         self.setter = setter(None) if setter else None
    #         self.feedback = None

    #     def new_setter(self, state): 
    #         self.setter = state

    #     def rename_var(self, text): 
    #         self.output = text

    #     def set_feedback(self, text): 
    #         self.feedback = text
    #         return self.feedback

    #     def get_feedback(self):
    #         return self.feedback

    # efc = VariableGenerator('efc', task_1_variable_details)
    # sai = VariableGenerator('sai', 
    #                         task_1_variable_details,
    #                        )
    # unmet = VariableGenerator('unmet', task_1_variable_details)
    # merit = VariableGenerator('merit', task_1_variable_details)
    # pell_plus = VariableGenerator('pell_plus', task_1_variable_details)
    return


@app.cell
def _(correct, mo, reactive_dict, task_1_variable_details):

    #functions
    def var_selection_text_generator(choice:str)->str: 
        if choice == 'include': 
            insert_text = "🟢 **Include** the variable **as-is**."
        if choice == 'exclude':
            insert_text = "🔴 **Exclude** the variable **entirely**."
        if choice == 'flag': 
            insert_text = "🟡 **Flag** the variable **for Review**."
        if choice == 'audit': 
            insert_text = '🟠 **Keep** the variable **for Bias-Audit Only**.'
        if choice == 'flag_impr': 
            insert_text = '🟠 **Flag** the variable **for Data-Quality Improvement**.'
        if choice == 'exclude_unre': 
            insert_text == "🔴 **Exclude** the variable **due to unreliability**."
        if not choice:
            insert_text = "⚪️ **not yet selected**"
            return f"You have {insert_text} a variable option."
        return f"You decided to {insert_text}"


    def generate_detailed_feedback_text(obj): 
        name = obj.var_name
        title = task_1_variable_details[name]['title']
        getter = obj.getter()
        message = task_1_variable_details[title]['feedback']['initial'][getter] if getter else ''
        return f"""**{title}:** {message}"""


    def variable_selection_output(obj): 
        try:
            reactives = reactive_dict[obj.var_name]
            getter = obj.getter()
            content = mo.vstack([
                mo.md(obj.definition),
                mo.hstack([reactives['include'], reactives['exclude'], reactives['other']], gap='1rem')
            ])
            output = mo.vstack([
                mo.accordion({obj.title: content}),
                mo.md(f"""{var_selection_text_generator(getter)}"""),
                reactives['textbox'] if getter else ''
            ])
            return output
        except: 
            print(obj.var_name)

    def variable_selection_output_2(variable_details): 
        buttons = variable_details['reactivity']['buttons']
        title = variable_details['title']
        definition = variable_details['def']
        getter = variable_details['reactivity']['getter']
        textbox = variable_details['reactivity']['textbox']
        content = mo.vstack([
            mo.md(definition),
            mo.hstack([buttons['include'], buttons['exclude'], buttons['other']], gap='1rem')
        ])
        output = mo.vstack([
            mo.accordion({title: content}),
            mo.md(f"""{var_selection_text_generator(getter)}"""),
            textbox if getter else ''
        ])
        return output


    def generate_feedback(variable_options: dict[str|dict, str]):
        choice = variable_options['reactive_elements']['getter']
        if choice: 
            if choice in variable_options['feedback']['initial']:
                feedback_message = variable_options['feedback']['initial'][choice]
            else: 
                feedback_message = variable_options['feedback']['initial']['other']
        else: 
            feedback_message = ''
        return mo.md(f"""**{variable_options['background']['title']}:** {feedback_message}""")


    def generate_feedback_2(variable_options): 
        choice = variable_options['reactivity']['getter']
        feedback_message = variable_options['feedback'][choice] if choice else ''
        return mo.md(f"""**{variable_options['title']}:** {feedback_message}""")


    def decision_label(choice):
        if choice in ["include", "include_as_is", "include_as-is"]:
            return "Include"
        elif choice in ["flag", "flag_improvement", "audit_only"]:
            return "Flag"
        elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
            return "Exclude"
        else:
            return "No Selection"


    def gather_final_feedback(variable_settings, correct_list, incorrect):
        title = variable_settings['background']['title']
        choice = variable_settings['reactive_elements']['getter']
        if choice: 
            if choice not in ['include', 'exclude']: 
                choice = 'other'
            feedback = variable_settings['feedback']['final'][choice] 
            if feedback == correct:
                correct_list.append(title)
            else: 
                incorrect.append(mo.md(f"""**{title}**: {feedback}"""))
        else: 
            incorrect.append(mo.md(f"""**{title}**: No variable was selected."""))
        return correct_list, incorrect


    def format_final_feedback(correct, incorrect): 
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
        generate_feedback,
        variable_selection_output,
    )


@app.cell
def _(mo):
    mo.md(f"""
    ##task_1_definitions
    """)
    return


@app.cell
def task_1_variable_details():
    # pell_choice = get_pell_state()
    # efc_choice = get_efc_state()
    # sai_choice = get_sai_state()
    # unmet_choice = get_unmet_state()
    # merit_choice = get_merit_state()
    # pell_plus_choice = get_pell_plus_state()


    # task_1_variable_details = {
    #     'pell': {
    #         'background': {
    #             'title': 'Pell Status',
    #             'def': 'Whether a student receives a federal Pell Grant. New regulations restrict use of financial-aid data' 
    #                    'in predictive modeling.',
    #         },
    #         'reactive_elements': {
    #             'getter': get_pell_state(),
    #             'getter_var': pell_choice,
    #             'textbox': pell_textbox,
    #             'buttons': {
    #                 'include': pell_incl,
    #                 'exclude': pell_excl,
    #                 'other': pell_flag,
    #             },
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Including Pell Status violates current federal guidance and may expose the institution to penalties.'
    #                            'Consider aggregate reporting instead of individual-level use.',
    #                 'exclude': correct,
    #                 'other': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Including Pell Status violates current federal guidance and may expose the institution to penalties. "
    #                            "Consider aggregate reporting instead of individual-level use.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             }
    #         },
    #     },
    #     'efc': {
    #         'background': {
    #             'title': 'Expected Family Contribution (EFC)',
    #             'def':  'Amount a family is expected to contribute to education costs (legacy FAFSA metric). '
    #                     'Regulatory compliance requires excluding this sensitive financial information.',
    #         },
    #         'reactive_elements': {
    #             'getter': get_efc_state(),
    #             'getter_var': efc_choice,
    #             'textbox': efc_textbox,
    #             'buttons': {
    #                 'include': efc_incl,
    #                 'exclude': efc_excl,
    #                 'other': efc_flag,
    #             },
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'EFC is explicitly barred under 2024 Department of Education rules; '
    #                            'its inclusion would render the model non-compliant.',
    #                 'exclude': correct, 
    #                 'other': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "EFC is explicitly barred under 2024 Department of Education rules; "
    #                            "its inclusion would render the model non-compliant.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    #     'sai': {
    #         'background': {
    #             'title': "Student Aid Index (SAI)",
    #             'def': "A new metric from recent FAFSA changes that replaced EFC. Recent implementation means this data may not be available for all students in your historical dataset.",
    #         },
    #         'reactive_elements': {
    #             'getter': get_sai_state(),
    #             'getter_var': sai_choice,
    #             'textbox': sai_textbox,
    #             'buttons': {
    #                 'include': sai_incl,
    #                 'exclude': sai_excl,
    #                 'other': sai_flag,
    #             },
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'SAI is sensitive financial-aid data with incomplete coverage. Using it risks privacy '
    #                            'violations and injects missing-data bias.',
    #                 'exclude': correct,
    #                 'flag': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "SAI is sensitive financial-aid data with incomplete coverage. "
    #                            "Using it risks privacy violations and injects missing-data bias.",
    #                 'exclude': correct,
    #                 'other': correct,                
    #             },
    #         },
    #     },
    #     'unmet': {
    #         'background': {
    #             'title': "Unmet Need",
    #             'def': 'Gap between the cost of attendance and the student’s available resources. '
    #                    'Financial-stress indicator, but regulatory restrictions likely prohibit its use in individual-level models.',
    #         },
    #         'reactive_elements': {
    #             'getter': get_unmet_state(),
    #             'getter_var': unmet_choice,
    #             'textbox': unmet_textbox,
    #             'buttons': {
    #                 'include': unmet_incl,
    #                 'exclude': unmet_excl,
    #                 'other': unmet_flag,
    #             },
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Unmet Need combines multiple restricted data points. '
    #                            'Including it would contravene policy and amplify socioeconomic bias.',
    #                 'exclude': correct,
    #                 'other': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Unmet Need combines multiple restricted data points. "
    #                            "Including it would contravene policy and amplify socioeconomic bias.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    #     'merit': {
    #         'background': {
    #             'title': "Merit Award Amount",
    #             'def': 'Scholarship amounts awarded based on academic achievement rather than financial need. '
    #                    'Consider whether this variable primarily reflects prior achievement or introduces '
    #                    'socioeconomic factors into your model.',            
    #         },
    #         'reactive_elements': {
    #             'getter': get_merit_state(),
    #             'getter_var': merit_choice,
    #             'textbox': merit_textbox,
    #             'buttons': {
    #                 'include': merit_incl,
    #                 'exclude': merit_excl,
    #                 'other': merit_flag,
    #             },
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. '
    #                            'Use only with a strong equity justification.',
    #                 'exclude': correct,
    #                 'flag': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. "
    #                            "Use only with a strong equity justification.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    #     'pell_plus': {
    #         'background': {
    #             'title': "Pell Plus",
    #             'def': 'University matching funds that complement federal Pell Grants. '
    #                    'Financial-aid variables like this are likely subject to the same regulatory restrictions '
    #                    'as other financial data.',
    #         },
    #         'reactive_elements': {
    #             'getter': get_pell_plus_state(),
    #             'getter_var': pell_plus_choice,
    #             'textbox': pell_plus_textbox,
    #             'buttons': {
    #                 'include': pell_plus_incl,
    #                 'exclude': pell_plus_excl,
    #                 'other': pell_plus_flag,
    #             },
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Pell Plus directly signals Pell participation; individual-level use is restricted. '
    #                            'Exclude or seek explicit legal clearance.',
    #                 'exclude': correct,
    #                 'flag': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Pell Plus directly signals Pell participation; individual-level use is restricted. "
    #                            "Exclude or seek explicit legal clearance.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    # }
    return


@app.cell
def _(reactives):
    reactives
    # # pell_choice = get_pell_state()
    # # efc_choice = get_efc_state()
    # # sai_choice = get_sai_state()
    # # unmet_choice = get_unmet_state()
    # # merit_choice = get_merit_state()
    # # pell_plus_choice = get_pell_plus_state()

    # task_1_label = 'Flag for Review'
    # task_1_return = 'flag'

    # task_1_variable_details = {
    #     'pell': {
    #         'background': {
    #             'title': 'Pell Status',
    #             'def': 'Whether a student receives a federal Pell Grant. New regulations restrict use of financial-aid data' 
    #                    'in predictive modeling.',
    #         },
    #         'flag_options': {
    #             'label' : task_1_label,
    #             'return': task_1_return,
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Including Pell Status violates current federal guidance and may expose the institution to penalties.'
    #                            'Consider aggregate reporting instead of individual-level use.',
    #                 'exclude': correct,
    #                 'other': 'Flagged',

    #             },
    #             'final': {
    #                 'include': "Including Pell Status violates current federal guidance and may expose the institution to penalties. "
    #                            "Consider aggregate reporting instead of individual-level use.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             }
    #         },
    #     },
    #     'efc': {
    #         'background': {
    #             'title': 'Expected Family Contribution (EFC)',
    #             'def':  'Amount a family is expected to contribute to education costs (legacy FAFSA metric). '
    #                     'Regulatory compliance requires excluding this sensitive financial information.',
    #         },
    #         'flag_options': {
    #             'label' : task_1_label,
    #             'return': task_1_return,
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'EFC is explicitly barred under 2024 Department of Education rules; '
    #                            'its inclusion would render the model non-compliant.',
    #                 'exclude': correct, 
    #                 'other': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "EFC is explicitly barred under 2024 Department of Education rules; "
    #                            "its inclusion would render the model non-compliant.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    #     'sai': {
    #         'background': {
    #             'title': "Student Aid Index (SAI)",
    #             'def': "A new metric from recent FAFSA changes that replaced EFC. Recent implementation means this data may not be available for all students in your historical dataset.",
    #         },
    #         'flag_options': {
    #             'label' : task_1_label,
    #             'return': task_1_return,
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'SAI is sensitive financial-aid data with incomplete coverage. Using it risks privacy '
    #                            'violations and injects missing-data bias.',
    #                 'exclude': correct,
    #                 'flag': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "SAI is sensitive financial-aid data with incomplete coverage. "
    #                            "Using it risks privacy violations and injects missing-data bias.",
    #                 'exclude': correct,
    #                 'other': correct,                
    #             },
    #         },
    #     },
    #     'unmet': {
    #         'background': {
    #             'title': "Unmet Need",
    #             'def': 'Gap between the cost of attendance and the student’s available resources. '
    #                    'Financial-stress indicator, but regulatory restrictions likely prohibit its use in individual-level models.',
    #         },
    #         'flag_options': {
    #             'label' : task_1_label,
    #             'return': task_1_return,
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Unmet Need combines multiple restricted data points. '
    #                            'Including it would contravene policy and amplify socioeconomic bias.',
    #                 'exclude': correct,
    #                 'other': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Unmet Need combines multiple restricted data points. "
    #                            "Including it would contravene policy and amplify socioeconomic bias.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    #     'merit': {
    #         'background': {
    #             'title': "Merit Award Amount",
    #             'def': 'Scholarship amounts awarded based on academic achievement rather than financial need. '
    #                    'Consider whether this variable primarily reflects prior achievement or introduces '
    #                    'socioeconomic factors into your model.',            
    #         },
    #         'flag_options': {
    #             'label' : task_1_label,
    #             'return': task_1_return,
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. '
    #                            'Use only with a strong equity justification.',
    #                 'exclude': correct,
    #                 'flag': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. "
    #                            "Use only with a strong equity justification.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    #     'pell_plus': {
    #         'background': {
    #             'title': "Pell Plus",
    #             'def': 'University matching funds that complement federal Pell Grants. '
    #                    'Financial-aid variables like this are likely subject to the same regulatory restrictions '
    #                    'as other financial data.',
    #         },
    #         'flag_options': {
    #             'label' : task_1_label,
    #             'return': task_1_return,
    #         },
    #         'feedback': {
    #             'initial': {
    #                 'include': 'Pell Plus directly signals Pell participation; individual-level use is restricted. '
    #                            'Exclude or seek explicit legal clearance.',
    #                 'exclude': correct,
    #                 'flag': 'Flagged',
    #             },
    #             'final': {
    #                 'include': "Pell Plus directly signals Pell participation; individual-level use is restricted. "
    #                            "Exclude or seek explicit legal clearance.",
    #                 'exclude': correct,
    #                 'other': correct,
    #             },
    #         },
    #     },
    # }
    return


@app.cell
def task_1_variable_status(
    existing_variable_objects,
    mo,
    variable_selection_output,
):
    task_1_display_output = [variable_selection_output(item) for item in existing_variable_objects]

    mo.output.replace(
        mo.vstack(task_1_display_output)
    )
    return


@app.cell
def task_1_detailed_feedback(generate_feedback, mo, task_1_variable_details):
    task_1_feedback = [generate_feedback(task_1_variable_details[key]) for key in task_1_variable_details]

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
def anchor_task_2(mo):
    mo.Html('<div id="task_2"></div>')
    return


@app.cell
def task_2(mo):
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
def _(mo, textbox_text_boilerplate):
    #task 2

    #getters and setters
    get_race_choice, set_race_choice = mo.state(None)
    get_gender_choice, set_gender_choice = mo.state(None)
    get_age_choice, set_age_choice = mo.state(None)
    get_pronoun_choice, set_pronoun_choice = mo.state(None)


    #buttons
    #button_labels
    task_2_labels = {'include': 'Include As-Is', 'exclude': 'Exclude Entirely', 'audit': 'Keep for Bias-Audit Only'}

    #race
    race_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_race_choice('include'))
    race_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_race_choice('audit'))
    race_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_race_choice('exclude'))

    #gender
    gender_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_gender_choice('include'))
    gender_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_gender_choice('audit'))
    gender_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_gender_choice('exclude'))

    #age
    age_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_age_choice('include'))
    age_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_age_choice('audit'))
    age_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_age_choice('exclude'))

    #pronouns
    pronoun_incl = mo.ui.run_button(label=task_2_labels['include'], kind='success', on_change=lambda _: set_pronoun_choice('include'))
    pronoun_audit = mo.ui.run_button(label=task_2_labels['audit'], kind='warn', on_change=lambda _: set_pronoun_choice('audit'))
    pronoun_excl = mo.ui.run_button(label=task_2_labels['exclude'], kind='danger', on_change=lambda _: set_pronoun_choice('exclude'))

    #textboxes
    race_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Race selection", rows=4)
    gender_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Gender selection", rows=4)
    age_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Age selection", rows=4)
    pronoun_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Preferred Pronouns selection", rows=4)
    return (
        age_audit,
        age_excl,
        age_incl,
        age_textbox,
        gender_audit,
        gender_excl,
        gender_incl,
        gender_textbox,
        get_age_choice,
        get_gender_choice,
        get_pronoun_choice,
        get_race_choice,
        pronoun_audit,
        pronoun_excl,
        pronoun_incl,
        pronoun_textbox,
        race_audit,
        race_excl,
        race_incl,
        race_textbox,
    )


@app.cell
def _(mo):
    mo.md("""
    ##task_2_definitions
    """)
    return


@app.cell
def _(
    age_audit,
    age_excl,
    age_incl,
    age_textbox,
    correct,
    gender_audit,
    gender_excl,
    gender_incl,
    gender_textbox,
    get_age_choice,
    get_gender_choice,
    get_pronoun_choice,
    get_race_choice,
    pronoun_audit,
    pronoun_excl,
    pronoun_incl,
    pronoun_textbox,
    race_audit,
    race_excl,
    race_incl,
    race_textbox,
):
    task_2_variable_details = {
        'race': {
            'background': {
                'title': "Race",
                'def': "Student’s self-reported racial/ethnic identity. Used during exploratory data analysis "
                       "but removed before predictive modeling.",
            },
            'reactive_elements': {
                'getter': get_race_choice(),
                'textbox': race_textbox,
                'buttons': {
                    'include': race_incl,
                    'exclude': race_excl,
                    'other': race_audit,
                },
            },
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
            'background': {
                'title': "Gender",
                'def': "Student’s gender identity as reported during application. "
                       "Protected class variable that raises ethical considerations.",
            },
            'reactive_elements': {
                'getter': get_gender_choice(),
                'textbox': gender_textbox,
                'buttons': {
                    'include': gender_incl,
                    'exclude': gender_excl,
                    'other': gender_audit,
                },
            },
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
            'background': {
                'title': "Age",
                'def': "Student’s age at enrollment. Flagged as protected class variable. "
                       "Consider whether age-based predictions might disadvantage non-traditional students while recognizing "
                       "that age can reflect meaningful differences in life circumstances.",
            },
            'reactive_elements': {
                'getter': get_age_choice(),
                'textbox': age_textbox,
                'buttons': {
                    'include': age_incl,
                    'exclude': age_excl,
                    'other': age_audit,
                },
            },
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
            'background': {
                'title': "Preferred Pronouns",
                'def': "Student-provided pronoun preference collected by campus climate office. Optional field with high missingness. Can affirm identity but is not a stable predictor of retention.",
            },
            'reactive_elements': {
                'getter': get_pronoun_choice(),
                'textbox': pronoun_textbox,
                'buttons': {
                    'include': pronoun_incl,
                    'exclude': pronoun_excl,
                    'other': pronoun_audit,
                },
            },
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
    }
    return (task_2_variable_details,)


@app.cell(hide_code=True)
def _():
    # task_2_variable_details = {
    #     'race': {
    #             'title': 'Race',
    #             'def': 'Student’s self-reported racial/ethnic identity. '
    #                    'Used during exploratory data analysis but removed before predictive modeling.',
    #             'getter': get_race_choice(),
    #             'textbox': race_textbox,
    #             'buttons': {
    #                 'include': race_incl,
    #                 'exclude': race_excl,
    #                 'other': race_audit,
    #             },
    #         'feedback': {
    #                 'include': 'Using Race as a predictive feature can embed historical inequities and violate '
    #                            'institutional policy. Retain only for bias-audit.',
    #                 'exclude': 'Without Race you lose the ability to audit fair outcomes across groups. '
    #                            'Best practice is to keep it for auditing while excluding it from model training.',
    #                 'audit': 'Right Choice',
    #             },
    #     },
    #     'gender': {
    #         'title': 'Gender',
    #         'def': '',
    #         'feedback': {
    #             'include': 'Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention.',
    #             'exclude': 'Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs.',
    #             'audit': 'Right Choice',
    #         },
    #         'getter': get_gender_choice(),
    #         'textbox': gender_textbox,
    #         'buttons': {
    #             'include': gender_incl,
    #             'exclude': gender_excl,
    #             'other': gender_audit,
    #         },
    #     },
    #     'age': {
    #         'title': 'Age',
    #         'def': 'Student’s age at enrollment. Flagged as protected class variable. Consider whether age-based predictions might disadvantage non-traditional students while recognizing that age can reflect meaningful differences in life circumstances.',
    #         'feedback': {
    #             'include': 'Age may correlate with persistence but also with protected status (non-traditional learners). Document equity safeguards or shift to audit-only use.',
    #             'exclude': 'Excluding Age erases patterns relevant to adult learners and hampers fairness checks. Audit-only use is often a balanced choice.',
    #             'audit': 'Right Choice',
    #         },
    #         'getter': get_age_choice(),
    #         'textbox': age_textbox,
    #         'buttons': {
    #             'include': age_incl,
    #             'exclude': age_excl,
    #             'other': age_audit,
    #         },
    #     },
    #     'pronouns': {
    #         'title': 'Preferred Pronouns',
    #         'def': 'Student-provided pronoun preference collected by campus climate office. Optional field with high missingness. Can affirm identity but is not a stable predictor of retention.',
    #         'feedback': {
    #             'include': 'Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. Exclude or store only for awareness training, not analytics.',
    #             'exclude': 'Right Choice',
    #             'audit': 'Pronoun data lack completeness and standardization, limiting audit utility. Exclusion is usually appropriate.',
    #         },
    #         'getter': get_pronoun_choice(),
    #         'textbox': pronoun_textbox,
    #         'buttons': {
    #             'include': pronoun_incl,
    #             'exclude': pronoun_excl,
    #             'other': pronoun_audit,
    #         },
    #     },
    # }
    return


@app.cell(hide_code=True)
def _(task_2_variable_details):
    def varprint(var): 
        print((f"'{var}': ""{"))
    def closeout(): 
        print('},')

    print('task_2a_variable_details = {')
    for k in task_2_variable_details: 
        curr = task_2_variable_details[k]
        varprint(k)
        print("'background': {")
        print(f"""'title': "{curr['title']}",""")
        print(f"""'def': "{curr['def']}",""")
        closeout()
        varprint('reactive_elements')
        print(f"""'getter': get_{k}_choice(),""")
        print(f"""'textbox': {k}_textbox,""")
        varprint('buttons')
        print(f"""'include': {k}_incl,""")
        print(f"""'exclude': {k}_excl,""")
        print(f"""'other': {k}_audit,""")
        closeout()
        closeout()
        varprint('feedback')
        varprint('initial')
        print(f"""'include': "{curr['feedback']['include']}",""")
        print(f"""'exclude': "{curr['feedback']['exclude']}",""")
        print(f"""'other': "{curr['feedback']['audit']}",""")
        closeout()
        varprint('final')
        print(f"""'initial': '',""")
        print(f"""'exclude': '',""")
        print(f"""'other': '',""")
        closeout()
        closeout()
        closeout()

    return


@app.cell
def _(mo, task_2_variable_details, variable_selection_output):
    task_2_display_output = [variable_selection_output(task_2_variable_details[key]) for key in task_2_variable_details]

    mo.output.replace(
        mo.vstack(task_2_display_output)
    )
    return


@app.cell
def _(generate_feedback, mo, task_2_variable_details):
    task_2_feedback = [generate_feedback(task_2_variable_details[key]) for key in task_2_variable_details]

    task_2_content_detail_feedback = mo.vstack(task_2_feedback)

    mo.accordion({"Detailed Feedback": task_2_content_detail_feedback})
    return


@app.cell
def section_separator(mo):
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell
def anchor_task_3(mo):
    mo.Html('<div id="task_3"></div>')
    return


@app.cell
def task_3(mo):
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


@app.cell
def _(mo, textbox_text_boilerplate):
    #task_3

    #getters and setters
    get_gpa_choice, set_gpa_choice = mo.state(None)
    get_scores_choice, set_scores_choice = mo.state(None)
    get_midterms_choice, set_midterms_choice = mo.state(None)
    get_epr_choice, set_epr_choice = mo.state(None)
    get_printer_choice, set_printer_choice = mo.state(None)


    #buttons

    #labels
    task_3_labels = {'include': 'Include as-is', 'exclude': 'Exclude (too unreliable)', 'flag_impr': 'Flag for Data-Quality Improvement'}

    #gpa
    gpa_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_gpa_choice('include'))
    gpa_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_gpa_choice('exclude'))
    gpa_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_gpa_choice('flag_impr'))

    #test_scores
    scores_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_scores_choice('include'))
    scores_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_scores_choice('exclude'))
    scores_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_scores_choice('flag_impr'))


    #midterm grades
    midterms_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_midterms_choice('include'))
    midterms_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_midterms_choice('exclude'))
    midterms_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_midterms_choice('flag_impr'))

    #epr
    epr_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_epr_choice('include'))
    epr_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_epr_choice('exclude'))
    epr_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_epr_choice('flag_impr'))

    #printer
    printer_incl = mo.ui.run_button(label=task_3_labels['include'], kind='success', on_change=lambda _: set_printer_choice('include'))
    printer_excl = mo.ui.run_button(label=task_3_labels['exclude'], kind='danger', on_change=lambda _: set_printer_choice('exclude'))
    printer_flag = mo.ui.run_button(label=task_3_labels['flag_impr'], kind='warn', on_change=lambda _: set_printer_choice('flag_impr'))

    #textboxes
    gpa_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} High School GPA selection.")
    scores_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Test Scores selection.")
    midterms_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Midterm Grades selection.")
    epr_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Early Progress Reports selection.")
    printer_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Dorm Printer Usage selection.")
    return (
        epr_excl,
        epr_flag,
        epr_incl,
        epr_textbox,
        get_epr_choice,
        get_gpa_choice,
        get_midterms_choice,
        get_printer_choice,
        get_scores_choice,
        gpa_excl,
        gpa_flag,
        gpa_incl,
        gpa_textbox,
        midterms_excl,
        midterms_flag,
        midterms_incl,
        midterms_textbox,
        printer_excl,
        printer_flag,
        printer_incl,
        printer_textbox,
        scores_excl,
        scores_flag,
        scores_incl,
        scores_textbox,
    )


@app.cell
def _(mo):
    mo.md("""
    ##task_3_definitions
    """)
    return


@app.cell
def _(
    correct,
    epr_excl,
    epr_flag,
    epr_incl,
    epr_textbox,
    get_epr_choice,
    get_gpa_choice,
    get_midterms_choice,
    get_printer_choice,
    get_scores_choice,
    gpa_excl,
    gpa_flag,
    gpa_incl,
    gpa_textbox,
    midterms_excl,
    midterms_flag,
    midterms_incl,
    midterms_textbox,
    printer_excl,
    printer_flag,
    printer_incl,
    printer_textbox,
    scores_excl,
    scores_flag,
    scores_incl,
    scores_textbox,
):
    task_3_variable_details = {
        'gpa': {
            'background': {
                'title': "High School GPA",
                'def': "Student’s high-school grade-point average, a common predictor of college success. "
                       "This variable was unreliable due to reporting unreliability across high schools.",
            },
            'reactive_elements': {
                'getter': get_gpa_choice(),
                'textbox': gpa_textbox,
                'buttons': {
                    'include': gpa_incl,
                    'exclude': gpa_excl,
                    'other': gpa_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "High-school GPAs lack standardisation; predictive value may be swamped by noise. "
                               "Consider excluding or flagging for quality remediation.",
                    'exclude': "Removing High-School GPA sacrifices a widely used predictor. "
                               "Could a scaled or percentile version salvage reliability?",
                    'other': correct,
                },
                'final': {
                    'initial': "High-school GPAs lack standardisation; predictive value may be swamped by noise. "
                               "Consider excluding or flagging for quality remediation.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'scores': {
            'background': {
                'title': "Test Scores",
                'def': "Academic performance metrics from high school and standardised tests (SAT/ACT). "
                       "Due to test-optional policies implemented during COVID, scores may be missing for many students. "
                       "Creative solution to transform into a ‘test score submitted’ indicator leverages available "
                       "information while addressing systematic gaps.",
    },
            'reactive_elements': {
                'getter': get_scores_choice(),
                'textbox': scores_textbox,
                'buttons': {
                    'include': scores_incl,
                    'exclude': scores_excl,
                    'other': scores_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. "
                               "A submission indicator or audit flag may be safer.",
                    'exclude': "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. "
                               "Could you retain a binary ‘submitted’ flag instead?",
                    'other': correct,
                },
                'final': {
                    'initial': "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. "
                               "A submission indicator or audit flag may be safer.",
                    'exclude': "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. "
                               "Could you retain a binary ‘submitted’ flag instead?",
                    'other': correct,
                },
            },
        },
        'midterms': {
            'background': {
                'title': "Midterm Grades",
                'def': "Preliminary academic performance indicators halfway through the term. "
                       "Identified as valuable but not consistently available across courses.",
            },
            'reactive_elements': {
                'getter': get_midterms_choice(),
                'textbox': midterms_textbox,
                'buttons': {
                'include': midterms_incl,
                'exclude': midterms_excl,
                'other': midterms_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Mid-Term Grades appear only for certain courses, risking departmental bias. "
                               "Flag for quality improvement or exclude.",
                    'exclude': "Excluding Mid-Term Grades forfeits early academic-performance insight. "
                               "Could selective inclusion or data-quality work make it viable?",
                    'other': correct,
                },
                'final': {
                    'initial': "Mid-Term Grades appear only for certain courses, risking departmental bias. "
                               "Flag for quality improvement or exclude.",
                    'exclude': "Excluding Mid-Term Grades forfeits early academic-performance insight. "
                               "Could selective inclusion or data-quality work make it viable?",
                    'other': correct,
                },
            },
        },
        'epr': {
            'background': {
                'title': "Early Progress Reports",
                'def': "Faculty-submitted assessments of student performance early in the semester. "
                       "Reporting inconsistency means this potentially valuable early-warning indicator isn’t reliable enough "
                       "to include.",
            },
            'reactive_elements': {
                'getter': get_epr_choice(),
                'textbox': epr_textbox,
                'buttons': {
                    'include': epr_incl,
                    'exclude': epr_excl,
                    'other': epr_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion.",
                    'exclude': "You lose a proven early-alert signal. Engage stakeholders to improve reporting rather "
                               "than discard entirely.",
                    'other': correct,
                },
                'final': {
                    'initial': "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion.",
                    'exclude': "You lose a proven early-alert signal. "
                               "Engage stakeholders to improve reporting rather than discard entirely.",
                    'other': correct,
                },
            },
        },
        'printer': {
            'background': {
                'title': "Dorm Printer Usage",
                'def': "Weekly count of pages printed in residence-hall printers. "
                       "Logs are missing whenever printers are offline; many students use personal or library printers instead.",
            },
            'reactive_elements': {
                'getter': get_printer_choice(),
                'textbox': printer_textbox,
                'buttons': {
                    'include': printer_incl,
                    'exclude': printer_excl,
                    'other': printer_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. "
                               "Little theoretical link to persistence.",
                    'exclude': "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost.",
                    'other': "Appropriate—the variable is weakly linked to retention and suffers systemic gaps.",
                },
                'final': {
                    'initial': "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. "
                               "Little theoretical link to persistence.",
                    'exclude': correct,
                    'other': "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost.",
                },
            },
        },
    }
    return (task_3_variable_details,)


@app.cell
def _():
    #likely unneeded, kept until I can prove replacement code works
    # task_3_variable_details = {
    #     'gpa': {
    #         'title': 'High School GPA',
    #         'def': 'Student’s high-school grade-point average, a common predictor of college success. This variable was unreliable due to reporting unreliability across high schools.',
    #         'feedback': {
    #             'include': 'High-school GPAs lack standardisation; predictive value may be swamped by noise. Consider excluding or flagging for quality remediation.',
    #             'exclude':'Removing High-School GPA sacrifices a widely used predictor. Could a scaled or percentile version salvage reliability?',
    #             'flag_impr':'Right Call',
    #         },
    #         'getter': get_gpa_choice(),
    #         'textbox': gpa_textbox,
    #         'buttons': {
    #             'include': gpa_incl,
    #             'exclude': gpa_excl,
    #             'other': gpa_flag,
    #         },
    #     },
    #     'scores': {
    #         'title': 'Test Scores',
    #         'def': 'Academic performance metrics from high school and standardised tests (SAT/ACT). Due to test-optional policies implemented during COVID, scores may be missing for many students. Creative solution to transform into a ‘test score submitted’ indicator leverages available information while addressing systematic gaps.',
    #         'feedback': {
    #             'include': 'Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. A submission indicator or audit flag may be safer.',
    #             'exclude': 'Dropping Test Scores ignores a potentially strong signal for the subset who submitted. Could you retain a binary ‘submitted’ flag instead?',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_scores_choice(),
    #         'textbox': scores_textbox,
    #         'buttons': {
    #             'include': scores_incl,
    #             'exclude': scores_excl,
    #             'other': scores_flag,
    #         },
    #     },
    #     'midterms': {
    #         'title': 'Midterm Grades',
    #         'def': 'Preliminary academic performance indicators halfway through the term. Identified as valuable but not consistently available across courses.',
    #         'feedback': {
    #             'include': 'Mid-Term Grades appear only for certain courses, risking departmental bias. Flag for quality improvement or exclude.',
    #             'exclude': 'Excluding Mid-Term Grades forfeits early academic-performance insight. Could selective inclusion or data-quality work make it viable?',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_midterms_choice(),
    #         'textbox': midterms_textbox,
    #         'buttons': {
    #             'include': midterms_incl,
    #             'exclude': midterms_excl,
    #             'other': midterms_flag,
    #         },
    #     },
    #     'epr': {
    #         'title': 'Early Progress Reports',
    #         'def': 'Faculty-submitted assessments of student performance early in the semester. Reporting inconsistency means this potentially valuable early-warning indicator isn’t reliable enough to include.',
    #         'feedback': {
    #             'include': 'Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion.',
    #             'exclude': 'You lose a proven early-alert signal. Engage stakeholders to improve reporting rather than discard entirely.',
    #             'flag_impr': 'Right Call',
    #         },
    #         'getter': get_epr_choice(),
    #         'textbox': epr_textbox,
    #         'buttons': {
    #             'include': epr_incl,
    #             'exclude': epr_excl,
    #             'other': epr_flag,
    #         },
    #     },
    #     'printer': {
    #         'title': 'Dorm Printer Usage',
    #         'def': 'Weekly count of pages printed in residence-hall printers. Logs are missing whenever printers are offline; many students use personal or library printers instead.',
    #         'feedback': {
    #             'include':'Printer logs cover only a subset of students and machines, yielding noisy, biased counts. Little theoretical link to persistence.',
    #             'exclude':'Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost.',
    #             'flag_impr':'Appropriate—the variable is weakly linked to retention and suffers systemic gaps.',
    #         },
    #         'getter': get_printer_choice(),
    #         'textbox': printer_textbox,
    #         'buttons': {
    #             'include': printer_incl,
    #             'exclude': printer_excl,
    #             'other': printer_flag,
    #         },
    #     },    
    # }
    return


@app.cell
def _(mo, task_3_variable_details, variable_selection_output):
    task_3_display_output = [variable_selection_output(task_3_variable_details[key]) for key in task_3_variable_details]

    mo.output.replace(
        mo.vstack(task_3_display_output)
    )
    return


@app.cell
def _(generate_feedback, mo, task_3_variable_details):
    task_3_feedback = [generate_feedback(task_3_variable_details[key]) for key in task_3_variable_details]

    task_3_content_detail_feedback = mo.vstack(task_3_feedback)

    mo.accordion({"Detailed Feedback": task_3_content_detail_feedback})
    return


@app.cell
def section_separator(mo):
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell
def anchor_task_4(mo):
    mo.Html('<div id="task_4"></div>')
    return


@app.cell
def task_4(mo):
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


@app.cell
def _(mo, set_firstgen_choice, textbox_text_boilerplate):
    #task_4

    #getters_and_setters
    get_legacy_choice, set_legacy_choice = mo.state(None)
    get_athlete_choice, set_athlete_choice = mo.state(None)
    get_firstgen_choice, set_firstget_choice = mo.state(None)
    get_distance_choice, set_distance_choice = mo.state(None)
    get_credits_choice, set_credits_choice = mo.state(None)
    get_housing_choice, set_housing_choice = mo.state(None)
    get_residency_choice, set_residency_choice = mo.state(None)
    get_origins_choice, set_origins_choice = mo.state(None)
    get_transfer_choice, set_transfer_choice = mo.state(None)
    get_extracurricular_choice, set_extracurricular_choice = mo.state(None)
    get_wi_fi_choice, set_wi_fi_choice = mo.state(None)

    #buttons
    #labels 
    task_4_labels = {'include': 'Include as-is', 'exclude': 'Exclude (too unreliable)', 'other': 'Flag for Data-Quality Improvement'}

    #legacy_status
    legacy_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_legacy_choice('include'))
    legacy_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_legacy_choice('exclude'))
    legacy_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_legacy_choice('flag_impr'))

    #student_athlete_status
    athlete_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_athlete_choice('include'))
    athlete_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_athlete_choice('exclude'))
    athlete_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_athlete_choice('flag_impr'))

    #first_generation_student
    firstgen_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_firstgen_choice('include'))
    firstgen_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_firstgen_choice('exclude'))
    firstgen_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_firstgen_choice('flag_impr'))

    #distance_from_home
    distance_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_distance_choice('include'))
    distance_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_distance_choice('exclude'))
    distance_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_distance_choice('flag_impr'))

    #credits_after_add_drop
    credits_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_credits_choice('include'))
    credits_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_credits_choice('exclude'))
    credits_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_credits_choice('flag_impr'))

    #live_on_campus_or_commute
    housing_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_housing_choice('include'))
    housing_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_housing_choice('exclude'))
    housing_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_housing_choice('flag_impr'))

    #residency_in_state_out_of_state_international
    residency_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_residency_choice('include'))
    residency_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_residency_choice('exclude'))
    residency_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_residency_choice('flag_impr'))

    #urban_rural_suburban_origin
    origins_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_origins_choice('include'))
    origins_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_origins_choice('exclude'))
    origins_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_origins_choice('flag_impr'))

    #transfer_status
    transfer_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_transfer_choice('include'))
    transfer_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_transfer_choice('exclude'))
    transfer_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_transfer_choice('flag_impr'))

    #extracurricular_involvement
    extracurricular_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', 
                                            on_change=lambda _: set_extracurricular_choice('include'))
    extracurricular_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', 
                                            on_change=lambda _: set_extracurricular_choice('exclude'))
    extracurricular_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', 
                                            on_change=lambda _: set_extracurricular_choice('flag_impr'))

    #campus_wi_fi_gaming_network_participation
    wi_fi_incl = mo.ui.run_button(label=task_4_labels['include'], kind='success', on_change=lambda _: set_wi_fi_choice('include'))
    wi_fi_excl = mo.ui.run_button(label=task_4_labels['exclude'], kind='danger', on_change=lambda _: set_wi_fi_choice('exclude'))
    wi_fi_flag = mo.ui.run_button(label=task_4_labels['other'], kind='warn', on_change=lambda _: set_wi_fi_choice('flag_impr'))


    #textboxes
    legacy_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Legacy Status selection.")
    athlete_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Student Athlete Status selection.")
    firstgen_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} First-Generation Status selection.")
    distance_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Distance From Home selection.")
    credits_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Credits After Add/Drop selection.")
    housing_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Living On Campus or Commuter selection.")
    residency_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Residency (In-State / Out-of-State / International) selection.")
    origins_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Urban / Rural / Suburban Origin selection")
    transfer_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Transfer Status selection.")
    extracurricular_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Extracurricular Involvement selection.")
    wi_fi_textbox = mo.ui.text_area(label=f"{textbox_text_boilerplate} Campus Wi-Fi Gaming Network Participation selection.")
    return (
        athlete_excl,
        athlete_flag,
        athlete_incl,
        athlete_textbox,
        credits_excl,
        credits_flag,
        credits_incl,
        credits_textbox,
        distance_excl,
        distance_flag,
        distance_incl,
        distance_textbox,
        extracurricular_excl,
        extracurricular_flag,
        extracurricular_incl,
        extracurricular_textbox,
        firstgen_excl,
        firstgen_flag,
        firstgen_incl,
        firstgen_textbox,
        get_athlete_choice,
        get_credits_choice,
        get_distance_choice,
        get_extracurricular_choice,
        get_firstgen_choice,
        get_housing_choice,
        get_legacy_choice,
        get_origins_choice,
        get_residency_choice,
        get_transfer_choice,
        get_wi_fi_choice,
        housing_excl,
        housing_flag,
        housing_incl,
        housing_textbox,
        legacy_excl,
        legacy_flag,
        legacy_incl,
        legacy_textbox,
        origins_excl,
        origins_flag,
        origins_incl,
        origins_textbox,
        residency_excl,
        residency_flag,
        residency_incl,
        residency_textbox,
        transfer_excl,
        transfer_flag,
        transfer_incl,
        transfer_textbox,
        wi_fi_excl,
        wi_fi_flag,
        wi_fi_incl,
        wi_fi_textbox,
    )


@app.cell
def _(mo):
    mo.md("""
    ## Task 4 Definitions
    """)
    return


@app.cell
def _(
    athlete_excl,
    athlete_flag,
    athlete_incl,
    athlete_textbox,
    correct,
    credits_excl,
    credits_flag,
    credits_incl,
    credits_textbox,
    distance_excl,
    distance_flag,
    distance_incl,
    distance_textbox,
    extracurricular_excl,
    extracurricular_flag,
    extracurricular_incl,
    extracurricular_textbox,
    firstgen_excl,
    firstgen_flag,
    firstgen_incl,
    firstgen_textbox,
    get_athlete_choice,
    get_credits_choice,
    get_distance_choice,
    get_extracurricular_choice,
    get_firstgen_choice,
    get_housing_choice,
    get_legacy_choice,
    get_origins_choice,
    get_residency_choice,
    get_transfer_choice,
    get_wi_fi_choice,
    housing_excl,
    housing_flag,
    housing_incl,
    housing_textbox,
    legacy_excl,
    legacy_flag,
    legacy_incl,
    legacy_textbox,
    origins_excl,
    origins_flag,
    origins_incl,
    origins_textbox,
    residency_excl,
    residency_flag,
    residency_incl,
    residency_textbox,
    transfer_excl,
    transfer_flag,
    transfer_incl,
    transfer_textbox,
    wi_fi_excl,
    wi_fi_flag,
    wi_fi_incl,
    wi_fi_textbox,
):
    task_4_variable_details = {
        'legacy': {
            'background': {
                'title': "Legacy Status",
                'def': "Whether the student has family members who previously attended the university. "
                       "May indicate stronger institutional ties.",
            },
            'reactive_elements': {
                'getter': get_legacy_choice(),
                'textbox': legacy_textbox,
                'buttons': {
                    'include': legacy_incl,
                    'exclude': legacy_excl,
                    'other': legacy_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Legacy Status may encode privilege and could unfairly prioritise well-connected students. "
                               "Document why its predictive gain outweighs equity concerns.",
                    'exclude': "You removed a factor linked to institutional attachment. "
                               "Could advisors design fair interventions if they knew a student lacked legacy ties?",
                    'other': correct,
                },
                'final': {
                    'initial': "Legacy Status may encode privilege and could unfairly prioritise well-connected students. "
                               "Document why its predictive gain outweighs equity concerns.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
        'athlete': {
            'background': {
                'title': "Student Athlete Status",
                'def': "Whether the student participates in university athletics. "
                       "May indicate additional support structures but also time commitments.",
            },
            'reactive_elements': {
                'getter': get_athlete_choice(),
                'textbox': athlete_textbox,
                'buttons': {
                    'include': athlete_incl,
                    'exclude': athlete_excl,
                    'other': athlete_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. "
                               "Ensure interventions add value.",
                    'exclude': "Athletes juggle academics and sport travel. "
                               "Excluding this variable may hide a known risk group lacking time for coursework.",
                    'other': correct,
                },
                'final': {
                    'initial': "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. "
                               "Ensure interventions add value.",
                    'exclude': "Athletes juggle academics and sport travel. "
                               "Excluding this variable may hide a known risk group lacking time for coursework.",
                    'other': correct,
                },
            },
        },
        'firstgen': {
            'background': {
                'title': "First Generation Status",
                'def': "Indicates if the student is the first in their family to attend college; "
                       "may reflect differences in familiarity with college processes.",
            },
            'reactive_elements': {
                'getter': get_firstgen_choice(),
                'textbox': firstgen_textbox,
                'buttons': {
                    'include': firstgen_incl,
                    'exclude': firstgen_excl,
                    'other': firstgen_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Good call—first-gen status supports equity-minded outreach. "
                               "Be sure to explain positive, not deficit-based, interventions.",
                    'exclude': "First-generation students often benefit from navigational support. "
                               "Omitting this variable could undermine equity goals.",
                    'other': correct,
                },
                'final': {
                    'initial': "Good call—first-gen status supports equity-minded outreach. "
                               "Be sure to explain positive, not deficit-based, interventions.",
                    'exclude': "First-generation students often benefit from navigational support. "
                               "Omitting this variable could undermine equity goals.",
                    'other': correct,
                },
            },
        },
        'distance': {
            'background': {
                'title': "Distance From Home",
                'def': "Calculated metric based on student’s home address and campus location; "
                       "privacy-preserving alternative to ZIP codes.",
            },
            'reactive_elements': {
                'getter': get_distance_choice(),
                'textbox': distance_textbox,
                'buttons': {
                    'include': distance_incl,
                    'exclude': distance_excl,
                    'other': distance_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Distance correlates with homesickness and travel cost but offers limited intervention levers. "
                               "Note whether actionable support exists (e.g., travel grants).",
                    'exclude': "Ignoring Distance removes insight into geographically isolated students "
                               "who may need community-building initiatives.",
                    'other': correct,
                },
                'final': {
                    'initial': "Distance correlates with homesickness and travel cost but offers limited intervention levers. "
                               "Note whether actionable support exists (e.g., travel grants).",
                    'exclude': "Ignoring Distance removes insight into geographically isolated students "
                               "who may need community-building initiatives.",
                    'other': correct,
                },
            },
        },
        'credits': {
            'background': {
                'title': "Credits After Add/Drop",
                'def': "Credit hours the student is taking after the official add/drop deadline; "
                       "may reflect adjustment to academic realities.",
            },
            'reactive_elements': {
                'getter': get_credits_choice(),
                'textbox': credits_textbox,
                'buttons': {
                    'include': credits_incl,
                    'exclude': credits_excl,
                    'other': credits_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Strong early signal of load management issues. Advisors can act quickly—solid choice.",
                    'exclude': "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value.",
                    'other': correct,
                },
                'final': {
                    'initial': "Strong early signal of load management issues. Advisors can act quickly—solid choice.",
                    'exclude': "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value.",
                    'other': correct,
                },
            },
        },
        'housing': {
            'background': {
                'title': "Live On Campus or Commuter",
                'def': "Housing status affects integration into campus life and access to resources.",
            },
            'reactive_elements': {
                'getter': get_housing_choice(),
                'textbox': housing_textbox,
                'buttons': {
                    'include': housing_incl,
                    'exclude': housing_excl,
                    'other': housing_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Useful and actionable—commuters may need remote-friendly support. "
                               "Ensure interventions respect time and travel constraints.",
                    'exclude': "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk.",
                    'other': correct,
                },
                'final': {
                    'initial': "Useful and actionable—commuters may need remote-friendly support. "
                               "Ensure interventions respect time and travel constraints.",
                    'exclude': "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk.",
                    'other': correct,
                },
            },
        },
        'residency': {
            'background': {
                'title': "Residency (In-State / Out-of-State / International)",
                'def': "Affects tuition rates and connection to campus.",
            },
            'reactive_elements': {
                'getter': get_residency_choice(),
                'textbox': residency_textbox,
                'buttons': {
                    'include': residency_incl,
                    'exclude': residency_excl,
                    'other': residency_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Residency drives cost burden; "
                               "interventions must avoid stereotyping out-of-state students as less committed.",
                    'exclude': "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups.",
                    'other': correct,
                },
                'final': {
                    'initial': "Residency drives cost burden; "
                               "interventions must avoid stereotyping out-of-state students as less committed.",
                    'exclude': "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups.",
                    'other': correct,
                },
            },
        },
        'origins': {
            'background': {
                'title': "Urban / Rural / Suburban Origins",
                'def': "Classification of student’s home community; derived from heuristics.",
            },
            'reactive_elements': {
                'getter': get_origins_choice(),
                'textbox': origins_textbox,
                'buttons': {
                    'include': origins_incl,
                    'exclude': origins_excl,
                    'other': origins_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Heuristic classification may mislabel students; validate definitions or risk noisy signals.",
                    'exclude': "Campus adjustment often differs by origin. "
                               "Excluding could overlook rural-to-urban transition challenges.",
                    'other': correct,
                },
                'final': {
                    'initial': "Heuristic classification may mislabel students; validate definitions or risk noisy signals.",
                    'exclude': "Campus adjustment often differs by origin. "
                               "Excluding could overlook rural-to-urban transition challenges.",
                    'other': correct,
                },
            },
        },
        'transfer': {
            'background': {
                'title': "Transfer Status",
                'def': "Whether the student transferred from another institution versus starting as a first-year.",
            },
            'reactive_elements': {
                'getter': get_transfer_choice(),
                'textbox': transfer_textbox,
                'buttons': {
                    'include': transfer_incl,
                    'exclude': transfer_excl,
                    'other': transfer_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant.",
                    'exclude': "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support.",
                    'other': correct,
                },
                'final': {
                    'initial': "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant.",
                    'exclude': "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support.",
                    'other': correct,
                },
            },
        },
        'extracurricular': {
            'background': {
                'title': "Extracurricular Involvement",
                'def': "Participation in clubs or other non-academic activities; data collection relies on self-reporting.",
            },
            'reactive_elements': {
                'getter': get_extracurricular_choice(),
                'textbox': extracurricular_textbox,
                'buttons': {
                    'include': extracurricular_incl,
                    'exclude': extracurricular_excl,
                    'other': extracurricular_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Self-report bias and missingness limit reliability; "
                               "document caveats to avoid overstating predictive value.",
                    'exclude': "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright.",
                    'other': correct,
                },
                'final': {
                    'initial': "Self-report bias and missingness limit reliability; "
                               "document caveats to avoid overstating predictive value.",
                    'exclude': "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright.",
                    'other': correct,
                },
            },
        },
        'wi_fi': {
            'background': {
                'title': "Campus-Wi-Fi Gaming Network Participation",
                'def': "Binary flag—student devices connected to high-traffic gaming ports for ≥ 5 hours/week during evenings.",
            },
            'reactive_elements': {
                'getter': get_wi_fi_choice(),
                'textbox': wi_fi_textbox,
                'buttons': {
                    'include': wi_fi_incl,
                    'exclude': wi_fi_excl,
                    'other': wi_fi_flag,
                },
            },
            'feedback': {
                'initial': {
                    'include': "Correlation to retention unproven; risk of pathologising hobby behaviour. "
                               "Provide theoretical justification or exclude.",
                    'exclude': "Sensible—no established link to academic persistence.",
                    'other': correct,
                },
                'final': {
                    'initial': "Correlation to retention unproven; risk of pathologising hobby behaviour. "
                               "Provide theoretical justification or exclude.",
                    'exclude': correct,
                    'other': correct,
                },
            },
        },
    }
    return (task_4_variable_details,)


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


@app.cell
def _(mo, task_4_variable_details, variable_selection_output):
    task_4_display_output = [variable_selection_output(task_4_variable_details[key]) for key in task_4_variable_details]

    mo.output.replace(
        mo.vstack(task_4_display_output)
    )
    return


@app.cell
def _(generate_feedback, mo, task_4_variable_details):
    task_4_feedback = [generate_feedback(task_4_variable_details[key]) for key in task_4_variable_details]

    task_4_content_detail_feedback = mo.vstack(task_4_feedback)

    mo.accordion({"Detailed Feedback": task_4_content_detail_feedback})
    return


@app.cell
def section_separator(mo):
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
    return


@app.cell
def wrapup_intro(
    decision_label,
    mo,
    task_1_variable_details,
    task_2_variable_details,
    task_3_variable_details,
    task_4_variable_details,
):
    # ---- Global submit state ----
    submit_state, set_submit_state = mo.state(False)

    # ---- Collect all choices ----
    variable_details = [task_1_variable_details, task_2_variable_details, task_3_variable_details, task_4_variable_details]
    all_choices = [variable_detail_dict[key]['reactive_elements']['getter'] for variable_detail_dict in variable_details for key in variable_detail_dict]

    # ---- Count included variables ----
    include_count = sum(1 for c in all_choices if decision_label(c) == "Include")

    # ---- Keep returning states for later use ----
    return (include_count,)


@app.cell
def wrapup_summary_table(
    decision_label,
    include_count,
    mo,
    task_1_variable_details,
    task_2_variable_details,
    task_3_variable_details,
    task_4_variable_details,
):
    grouped_rows = {
        'Regulatory Gate': [
            (decision_label(task_1_variable_details[key]['reactive_elements']['getter']),
             task_1_variable_details[key]['background']['title'])
            for key
            in task_1_variable_details
        ],
        'Protected-Attribute Gate': [
            (decision_label(task_2_variable_details[key]['reactive_elements']['getter']),
             task_2_variable_details[key]['background']['title'])
            for key
            in task_2_variable_details
        ],
        'Data-Reliability Gate': [
            (decision_label(task_3_variable_details[key]['reactive_elements']['getter']),
             task_3_variable_details[key]['background']['title'])
            for key
            in task_3_variable_details

        ],
        'Equity & Actionability Gate': [
            (decision_label(task_4_variable_details[key]['reactive_elements']['getter']),
             task_4_variable_details[key]['background']['title'])
            for key
            in task_4_variable_details
        ],
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
        f"**_Your model will use the {include_count} variables highlighted in green._** "
        "Is this acceptable, or would you like to revise your selections?"
    ),
        mo.Html(table_html)
    ])
    return


@app.cell
def _(mo):
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
def _(mo):
    mo.Html(f"""<hr style="border: 3px solid #4CAF50; margin-top:1rem; margin-bottom:1rem;">""")
    return


@app.cell
def _(mo):
    mo.Html(f"""<div style="text-align:center; color:#4CAF50; font-size:1.5rem; font-weight:bold; margin-bottom:1rem;">Final Feedback </div>""")
    return


@app.cell
def _(mo):
    mo.md(f"""
    ##task_1_final_feedback
    """)
    return


@app.cell
def _(
    format_final_feedback,
    gather_final_feedback,
    mo,
    task_heading_to_task_data,
):
    final_output = []

    for task_heading in task_heading_to_task_data: 
        variables = task_heading_to_task_data[task_heading]
        cor = []
        incor = []
        for final_variable in variables: 
            cor, incor = gather_final_feedback(variables[final_variable], cor, incor)
        final_task_output = format_final_feedback(cor, incor)
        final_output.append(mo.accordion({task_heading: final_task_output}))

    mo.vstack(final_output)
    return


@app.cell
def task_f(mo):
    get_prod_text, set_prod_text = mo.state("")
    get_refl_text, set_refl_text = mo.state("")

    mo.vstack([
        mo.md("## Placeholder for Product"),
        mo.Html("<div style='width:100%;'>"),  # force full-width container
        mo.ui.text_area(
            label="Enter your product notes here",
            value=get_prod_text(),
            on_change=lambda v: set_prod_text(v),
            rows=8,
        ),
        mo.Html("</div>"),

        mo.md("&nbsp;"),

        mo.md("## Placeholder for Learner Reflection"),
        mo.Html("<div style='width:100%;'>"),
        mo.ui.text_area(
            label="Please write your reflection here",
            value=get_refl_text(),
            on_change=lambda v: set_refl_text(v),
            rows=12,
        ),
        mo.Html("</div>"),

        mo.md("&nbsp;"),
    ])
    return


@app.cell
def pell_status():
    # content = mo.vstack([
    #     mo.md(
    #         "Whether a student receives a federal Pell Grant. "
    #         "New regulations restrict use of financial-aid data in predictive modeling."
    #     ),
    #     mo.hstack([pell_include, pell_exclude, pell_flag], gap="1rem"),
    # ])

    # mo.output.replace(
    #     mo.vstack([mo.accordion({"Pell Status": content}), mo.md(f"""{task_1_var_selection_text_generator(get_pell_state)}""")])
    # )
    # if get_pell_state()['boolean']: 
    #     mo.output.replace_at_index(pell_text, 1)
    return


@app.cell
def _():
    # efc_content = mo.vstack([
    #     mo.md(
    #         "Amount a family is expected to contribute to education costs "
    #         "(legacy FAFSA metric). Regulatory compliance requires excluding "
    #         "this sensitive financial information."
    #     ),
    #     mo.hstack([efc_include, efc_exclude, efc_flag], gap="1rem"),
    # ])
    # mo.output.replace(
    #     mo.vstack(
    #         mo.accordion({"Expected Family Contribution (EFC)": efc_content}),
    #         mo.md(f"")

    #     )
    # )
    return


@app.cell
def pell_justification():
    #  m 
    return


@app.cell
def efc_status():

    # # 1 reactive state for this variable
    # get_efc_choice, set_efc_choice = mo.state(None)

    # # 2 flag buttons
    # efc_include_btn = mo.ui.button(
    #     label="Include", kind="success", on_click=lambda _: set_efc_choice("include")
    # )
    # efc_exclude_btn = mo.ui.button(
    #     label="Exclude", kind="danger",  on_click=lambda _: set_efc_choice("exclude")
    # )
    # efc_flag_btn = mo.ui.button(
    #     label="Flag for Review", kind="warn", on_click=lambda _: set_efc_choice("flag")
    # )

    # # 3 put buttons in an accordion (or any layout you like)
    # efc_content = mo.vstack([
    #     mo.md(
    #         "Amount a family is expected to contribute to education costs "
    #         "(legacy FAFSA metric). Regulatory compliance requires excluding "
    #         "this sensitive financial information."
    #     ),
    #     mo.hstack([efc_include, efc_exclude, efc_flag], gap="1rem"),
    # ])
    # mo.accordion({"Expected Family Contribution (EFC)": efc_content})

    # # 4 return the getter so other cells can react to it
    return


@app.cell
def efc_feedback():

    # # 1 read the current flag
    # efc_choice = get_efc_choice()

    # # 2 maps for emoji and label
    # efc_emoji_map = {
    #     "include": "🟢",
    #     "exclude": "🔴",
    #     "flag":    "🟡",
    #     None:      "⚪️",
    # }
    # efc_text_map = {
    #     "include": "Include",
    #     "exclude": "Exclude",
    #     "flag":    "Flag for Review",
    #     None:      "no selection",
    # }

    # # 3 wrap in mo.md so this cell re-runs whenever choice changes
    # mo.md(f"You decided to {efc_emoji_map[efc_choice]} **{efc_text_map[efc_choice]}** the variable.")
    return


@app.cell
def efc_justification():
    # # 1 read current EFC selection
    # efc_text_choice = get_efc_choice()

    # # 2 state holder for the justification text
    # get_text_just_efc, set_text_just_efc = mo.state("")

    # # 3 show textarea only after user picks Include / Exclude / Flag
    # content_just_efc = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your EFC choice",
    #         value=get_text_just_efc(),
    #         on_change=lambda v: set_text_just_efc(v),
    #         rows=4,
    #     )
    #     if efc_text_choice is not None
    #     else mo.md("")          
    # )

    # content_just_efc
    return


@app.cell
def sai_status():
    # # 1) reactive state for SAI
    # get_sai_choice, set_sai_choice = mo.state(None)

    # # 2) flag buttons (all kwargs)
    # sai_inc_btn  = mo.ui.button(
    #     label="Include",
    #     kind="success",
    #     on_click=lambda _: set_sai_choice("include"),
    # )
    # sai_exc_btn  = mo.ui.button(
    #     label="Exclude",
    #     kind="danger",
    #     on_click=lambda _: set_sai_choice("exclude"),
    # )
    # sai_flag_btn = mo.ui.button(
    #     label="Flag for Review",
    #     kind="warn",
    #     on_click=lambda _: set_sai_choice("flag"),
    # )

    # # 3) accordion content
    # sai_content = mo.vstack([
    #     mo.md(
    #         "A new metric from recent FAFSA changes that replaced EFC. "
    #         "Recent implementation means this data may not be available for all "
    #         "students in your historical dataset."
    #     ),
    #     mo.hstack([sai_inc_btn, sai_exc_btn, sai_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Student Aid Index (SAI)": sai_content})

    # # 4) expose getter
    return


@app.cell
def sai_feedback():
    # # current flag
    # sai_choice = get_sai_choice()

    # # emoji / text maps
    # sai_emoji_map = {
    #     "include": "🟢",
    #     "exclude": "🔴",
    #     "flag":    "🟡",
    #     None:      "⚪️",
    # }
    # sai_text_map = {
    #     "include": "Include",
    #     "exclude": "Exclude",
    #     "flag":    "Flag for Review",
    #     None:      "no selection",
    # }

    # # show live feedback line
    # mo.md(
    #     f"You decided to {sai_emoji_map[sai_choice]} "
    #     f"**{sai_text_map[sai_choice]}** the variable."
    # )
    return


@app.cell
def sai_justification():
    # # read current SAI selection (unique local name)
    # sai_selected_flag = get_sai_choice()

    # # state holder for SAI justification text
    # get_text_just_sai, set_text_just_sai = mo.state("")

    # # show textarea only after a flag is chosen
    # content_just_sai = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your SAI choice",
    #         value=get_text_just_sai(),
    #         on_change=lambda v: set_text_just_sai(v),
    #         rows=4,
    #     )
    #     if sai_selected_flag is not None
    #     else mo.md("")          # nothing yet
    # )

    # content_just_sai
    return


@app.cell
def unmet_status():
    # # reactive state for Unmet Need
    # get_unmet_choice, set_unmet_choice = mo.state(None)

    # # buttons (all kwargs)
    # unmet_inc_btn  = mo.ui.button(
    #     label="Include",
    #     kind="success",
    #     on_click=lambda _: set_unmet_choice("include"),
    # )
    # unmet_exc_btn  = mo.ui.button(
    #     label="Exclude",
    #     kind="danger",
    #     on_click=lambda _: set_unmet_choice("exclude"),
    # )
    # unmet_flag_btn = mo.ui.button(
    #     label="Flag for Review",
    #     kind="warn",
    #     on_click=lambda _: set_unmet_choice("flag"),
    # )

    # # accordion content
    # unmet_content = mo.vstack([
    #     mo.md(
    #         "Gap between the cost of attendance and the student’s available resources. "
    #         "Financial-stress indicator, but regulatory restrictions likely prohibit "
    #         "its use in individual-level models."
    #     ),
    #     mo.hstack([unmet_inc_btn, unmet_exc_btn, unmet_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Unmet Need": unmet_content})

    # # expose getter
    return


@app.cell
def unmet_feedback():
    # unmet_choice = get_unmet_choice()

    # unmet_emoji_map = {
    #     "include": "🟢",
    #     "exclude": "🔴",
    #     "flag":    "🟡",
    #     None:      "⚪️",
    # }
    # unmet_text_map = {
    #     "include": "Include",
    #     "exclude": "Exclude",
    #     "flag":    "Flag for Review",
    #     None:      "no selection",
    # }

    # mo.md(
    #     f"You decided to {unmet_emoji_map[unmet_choice]} "
    #     f"**{unmet_text_map[unmet_choice]}** the variable."
    # )
    return


@app.cell
def unmet_justification():
    # unmet_selected_flag = get_unmet_choice()

    # # text state
    # get_text_just_unmet, set_text_just_unmet = mo.state("")

    # content_just_unmet = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Unmet Need choice",
    #         value=get_text_just_unmet(),
    #         on_change=lambda v: set_text_just_unmet(v),
    #         rows=4,
    #     )
    #     if unmet_selected_flag is not None
    #     else mo.md("")
    # )

    # content_just_unmet
    return


@app.cell
def merit_status():
    # # state for Merit Award Amount
    # get_merit_choice, set_merit_choice = mo.state(None)

    # # buttons
    # merit_inc_btn  = mo.ui.button(
    #     label="Include",
    #     kind="success",
    #     on_click=lambda _: set_merit_choice("include"),
    # )
    # merit_exc_btn  = mo.ui.button(
    #     label="Exclude",
    #     kind="danger",
    #     on_click=lambda _: set_merit_choice("exclude"),
    # )
    # merit_flag_btn = mo.ui.button(
    #     label="Flag for Review",
    #     kind="warn",
    #     on_click=lambda _: set_merit_choice("flag"),
    # )

    # # accordion content
    # merit_content = mo.vstack([
    #     mo.md(
    #         "Scholarship amounts awarded based on academic achievement rather than "
    #         "financial need. Consider whether this variable primarily reflects prior "
    #         "achievement or introduces socioeconomic factors into your model."
    #     ),
    #     mo.hstack([merit_inc_btn, merit_exc_btn, merit_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Merit Award Amount": merit_content})
    return


@app.cell
def merit_feedback():
    # merit_choice = get_merit_choice()

    # merit_emoji_map = {
    #     "include": "🟢",
    #     "exclude": "🔴",
    #     "flag":    "🟡",
    #     None:      "⚪️",
    # }
    # merit_text_map = {
    #     "include": "Include",
    #     "exclude": "Exclude",
    #     "flag":    "Flag for Review",
    #     None:      "no selection",
    # }

    # mo.md(
    #     f"You decided to {merit_emoji_map[merit_choice]} "
    #     f"**{merit_text_map[merit_choice]}** the variable."
    # )
    return


@app.cell
def merit_justification():
    # merit_selected_flag = get_merit_choice()

    # get_text_just_merit, set_text_just_merit = mo.state("")

    # content_just_merit = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Merit Award choice",
    #         value=get_text_just_merit(),
    #         on_change=lambda v: set_text_just_merit(v),
    #         rows=4,
    #     )
    #     if merit_selected_flag is not None
    #     else mo.md("")
    # )

    # content_just_merit
    return


@app.cell
def pplus_status():
    # # state for Pell Plus
    # get_pplus_choice, set_pplus_choice = mo.state(None)

    # # buttons
    # pplus_inc_btn  = mo.ui.button(
    #     label="Include",
    #     kind="success",
    #     on_click=lambda _: set_pplus_choice("include"),
    # )
    # pplus_exc_btn  = mo.ui.button(
    #     label="Exclude",
    #     kind="danger",
    #     on_click=lambda _: set_pplus_choice("exclude"),
    # )
    # pplus_flag_btn = mo.ui.button(
    #     label="Flag for Review",
    #     kind="warn",
    #     on_click=lambda _: set_pplus_choice("flag"),
    # )

    # # accordion content
    # pplus_content = mo.vstack([
    #     mo.md(
    #         "University matching funds that complement federal Pell Grants. "
    #         "Financial-aid variables like this are likely subject to the same "
    #         "regulatory restrictions as other financial data."
    #     ),
    #     mo.hstack([pplus_inc_btn, pplus_exc_btn, pplus_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Pell Plus": pplus_content})
    return


@app.cell
def pplus_feedback():
    # pplus_choice = get_pplus_choice()

    # pplus_emoji_map = {
    #     "include": "🟢",
    #     "exclude": "🔴",
    #     "flag":    "🟡",
    #     None:      "⚪️",
    # }
    # pplus_text_map = {
    #     "include": "Include",
    #     "exclude": "Exclude",
    #     "flag":    "Flag for Review",
    #     None:      "no selection",
    # }

    # mo.md(
    #     f"You decided to {pplus_emoji_map[pplus_choice]} "
    #     f"**{pplus_text_map[pplus_choice]}** the variable."
    # )
    return


@app.cell
def pplus_justification():
    # pplus_selected_flag = get_pplus_choice()

    # get_text_just_pplus, set_text_just_pplus = mo.state("")

    # content_just_pplus = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Pell Plus choice",
    #         value=get_text_just_pplus(),
    #         on_change=lambda v: set_text_just_pplus(v),
    #         rows=4,
    #     )
    #     if pplus_selected_flag is not None
    #     else mo.md("")
    # )

    # content_just_pplus
    return


@app.cell
def _():
    # mo.output.replace(
    #     mo.vstack(
    #         [mo.accordion({pell_plus_text['title']: pell_plus_content}), 
    #          mo.md(f"""{var_selection_text_generator(pell_plus_choice)}""")]
    #     )
    # )
    # if pell_plus_choice: 
    #     mo.output.replace_at_index(pell_plus_textbox, 1)
    # get_race_choice, set_race_choice = mo.state(None)

    # race_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_race_choice("include_as_is")
    # )
    # race_audit_btn = mo.ui.button(
    #     label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_race_choice("audit_only")
    # )
    # race_exc_btn = mo.ui.button(
    #     label="Exclude Entirely", kind="danger", on_click=lambda _: set_race_choice("exclude_entirely")
    # )
    # race_
    # race_content = mo.vstack([
    #     mo.md("Student’s self-reported racial/ethnic identity. Used during exploratory data analysis but removed before predictive modeling."),
    #     mo.hstack([race_inc_btn, race_audit_btn, race_exc_btn], gap="1rem"),
    # ])
    # mo.accordion({"Race": race_content})
    return


@app.cell
def race_feedback():
    # race_choice = get_race_choice()

    # race_emoji_map = {
    #     "include_as_is": "🟢",
    #     "audit_only": "🟠",
    #     "exclude_entirely": "🔴",
    #     None: "⚪️",
    # }
    # race_text_map = {
    #     "include_as_is": "Include as-is",
    #     "audit_only": "Keep for Bias-Audit Only",
    #     "exclude_entirely": "Exclude Entirely",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {race_emoji_map[race_choice]} **{race_text_map[race_choice]}** the variable.")
    return


@app.cell
def race_justification():
    # race_selected_flag = get_race_choice()
    # get_text_just_race, set_text_just_race = mo.state("")

    # content_just_race = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Race choice",
    #         value=get_text_just_race(),
    #         on_change=lambda v: set_text_just_race(v),
    #         rows=4,
    #     )
    #     if race_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_race
    return


@app.cell
def gender_status():
    # get_gender_choice, set_gender_choice = mo.state(None)

    # gender_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_gender_choice("include_as_is")
    # )
    # gender_audit_btn = mo.ui.button(
    #     label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_gender_choice("audit_only")
    # )
    # gender_exc_btn = mo.ui.button(
    #     label="Exclude Entirely", kind="danger", on_click=lambda _: set_gender_choice("exclude_entirely")
    # )

    # gender_content = mo.vstack([
    #     mo.md("Student’s gender identity as reported during application. Protected class variable that raises ethical considerations."),
    #     mo.hstack([gender_inc_btn, gender_audit_btn, gender_exc_btn], gap="1rem"),
    # ])
    # mo.accordion({"Gender": gender_content})
    return


@app.cell
def gender_feedback():
    # gender_choice = get_gender_choice()

    # gender_emoji_map = {
    #     "include_as_is": "🟢",
    #     "audit_only": "🟠",
    #     "exclude_entirely": "🔴",
    #     None: "⚪️",
    # }
    # gender_text_map = {
    #     "include_as_is": "Include as-is",
    #     "audit_only": "Keep for Bias-Audit Only",
    #     "exclude_entirely": "Exclude Entirely",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {gender_emoji_map[gender_choice]} **{gender_text_map[gender_choice]}** the variable.")
    return


@app.cell
def gender_justification():
    # gender_selected_flag = get_gender_choice()
    # get_text_just_gender, set_text_just_gender = mo.state("")

    # content_just_gender = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Gender choice",
    #         value=get_text_just_gender(),
    #         on_change=lambda v: set_text_just_gender(v),
    #         rows=4,
    #     )
    #     if gender_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_gender
    return


@app.cell
def age_status():
    # get_age_choice, set_age_choice = mo.state(None)

    # age_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_age_choice("include_as_is")
    # )
    # age_audit_btn = mo.ui.button(
    #     label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_age_choice("audit_only")
    # )
    # age_exc_btn = mo.ui.button(
    #     label="Exclude Entirely", kind="danger", on_click=lambda _: set_age_choice("exclude_entirely")
    # )

    # age_content = mo.vstack([
    #     mo.md("Student’s age at enrollment. Flagged as protected class variable. Consider whether age-based predictions might disadvantage non-traditional students while recognizing that age can reflect meaningful differences in life circumstances."),
    #     mo.hstack([age_inc_btn, age_audit_btn, age_exc_btn], gap="1rem"),
    # ])
    # mo.accordion({"Age": age_content})
    return


@app.cell
def age_feedback():
    # age_choice = get_age_choice()

    # age_emoji_map = {
    #     "include_as_is": "🟢",
    #     "audit_only": "🟠",
    #     "exclude_entirely": "🔴",
    #     None: "⚪️",
    # }
    # age_text_map = {
    #     "include_as_is": "Include as-is",
    #     "audit_only": "Keep for Bias-Audit Only",
    #     "exclude_entirely": "Exclude Entirely",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {age_emoji_map[age_choice]} **{age_text_map[age_choice]}** the variable.")
    return


@app.cell
def age_justification():
    # age_selected_flag = get_age_choice()
    # get_text_just_age, set_text_just_age = mo.state("")

    # content_just_age = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Age choice",
    #         value=get_text_just_age(),
    #         on_change=lambda v: set_text_just_age(v),
    #         rows=4,
    #     )
    #     if age_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_age
    return


@app.cell
def pronouns_status():
    # get_pronouns_choice, set_pronouns_choice = mo.state(None)

    # pronouns_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_pronouns_choice("include_as_is")
    # )
    # pronouns_audit_btn = mo.ui.button(
    #     label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_pronouns_choice("audit_only")
    # )
    # pronouns_exc_btn = mo.ui.button(
    #     label="Exclude Entirely", kind="danger", on_click=lambda _: set_pronouns_choice("exclude_entirely")
    # )

    # pronouns_content = mo.vstack([
    #     mo.md("Student-provided pronoun preference collected by campus climate office. Optional field with high missingness. Can affirm identity but is not a stable predictor of retention."),
    #     mo.hstack([pronouns_inc_btn, pronouns_audit_btn, pronouns_exc_btn], gap="1rem"),
    # ])
    # mo.accordion({"Preferred Pronouns": pronouns_content})
    return


@app.cell
def pronouns_feedback():
    # pronouns_choice = get_pronouns_choice()

    # pronouns_emoji_map = {
    #     "include_as_is": "🟢",
    #     "audit_only": "🟠",
    #     "exclude_entirely": "🔴",
    #     None: "⚪️",
    # }
    # pronouns_text_map = {
    #     "include_as_is": "Include as-is",
    #     "audit_only": "Keep for Bias-Audit Only",
    #     "exclude_entirely": "Exclude Entirely",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {pronouns_emoji_map[pronouns_choice]} **{pronouns_text_map[pronouns_choice]}** the variable.")
    return


@app.cell
def pronouns_justification():
    # pronouns_selected_flag = get_pronouns_choice()
    # get_text_just_pronouns, set_text_just_pronouns = mo.state("")

    # content_just_pronouns = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Preferred Pronouns choice",
    #         value=get_text_just_pronouns(),
    #         on_change=lambda v: set_text_just_pronouns(v),
    #         rows=4,
    #     )
    #     if pronouns_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_pronouns
    return


@app.cell
def _(mo):
    mo.md("""
    ## feedback text
    """)
    return


@app.cell
def detailed_feedback_task2():
    # # ----- Race message
    # race = get_race_choice()
    # if race == "include_as_is":
    #     msg_race = "Using Race as a predictive feature can embed historical inequities and violate institutional policy. Retain only for bias-audit."
    # elif race == "audit_only":
    #     msg_race = "Right call"
    # elif race == "exclude_entirely":
    #     msg_race = "Without Race you lose the ability to audit fair outcomes across groups. Best practice is to keep it for auditing while excluding it from model training."
    # else:
    #     msg_race = ""

    # # ----- Gender message
    # gender = get_gender_choice()
    # if gender == "include_as_is":
    #     msg_gender = "Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention."
    # elif gender == "audit_only":
    #     msg_gender = "Right call"
    # elif gender == "exclude_entirely":
    #     msg_gender = "Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs."
    # else:
    #     msg_gender = ""

    # # ----- Age message
    # age = get_age_choice()
    # if age == "include_as_is":
    #     msg_age = "Age may correlate with persistence but also with protected status (non-traditional learners). Document equity safeguards or shift to audit-only use."
    # elif age == "audit_only":
    #     msg_age = "Right call"
    # elif age == "exclude_entirely":
    #     msg_age = "Excluding Age erases patterns relevant to adult learners and hampers fairness checks. Audit-only use is often a balanced choice."
    # else:
    #     msg_age = ""

    # # ----- Pronouns message
    # pronouns = get_pronouns_choice()
    # if pronouns == "include_as_is":
    #     msg_pronouns = "Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. Exclude or store only for awareness training, not analytics."
    # elif pronouns == "audit_only":
    #     msg_pronouns = "Pronoun data lack completeness and standardization, limiting audit utility. Exclusion is usually appropriate."
    # elif pronouns == "exclude_entirely":
    #     msg_pronouns = "Right call"
    # else:
    #     msg_pronouns = ""

    # content_detail_feedback2 = mo.vstack([
    #     mo.md(f"**Race:** {msg_race}"),
    #     mo.md(f"**Gender:** {msg_gender}"),
    #     mo.md(f"**Age:** {msg_age}"),
    #     mo.md(f"**Preferred Pronouns:** {msg_pronouns}"),
    # ])

    # mo.accordion({"Detailed Feedback – Task 2": content_detail_feedback2})
    return


@app.cell
def hsgpa_status():
    # get_hsgpa_choice, set_hsgpa_choice = mo.state(None)

    # hsgpa_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_hsgpa_choice("include_as_is")
    # )
    # hsgpa_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_hsgpa_choice("exclude_unreliable")
    # )
    # hsgpa_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_hsgpa_choice("flag_improvement")
    # )

    # hsgpa_content = mo.vstack([
    #     mo.md(
    #         "Student’s high-school grade-point average, a common predictor of college success. "
    #         "This variable was unreliable due to reporting unreliability across high schools."
    #     ),
    #     mo.hstack([hsgpa_inc_btn, hsgpa_exc_btn, hsgpa_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"High-School GPA": hsgpa_content})
    return


@app.cell
def hsgpa_feedback():
    # hsgpa_choice = get_hsgpa_choice()

    # hsgpa_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # hsgpa_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {hsgpa_emoji_map[hsgpa_choice]} **{hsgpa_text_map[hsgpa_choice]}** the variable.")
    return


@app.cell
def hsgpa_justification():
    # hsgpa_selected_flag = get_hsgpa_choice()
    # get_text_just_hsgpa, set_text_just_hsgpa = mo.state("")

    # content_just_hsgpa = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your High-School GPA choice",
    #         value=get_text_just_hsgpa(),
    #         on_change=lambda v: set_text_just_hsgpa(v),
    #         rows=4,
    #     )
    #     if hsgpa_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_hsgpa
    return


@app.cell
def tests_status():
    # get_tests_choice, set_tests_choice = mo.state(None)

    # tests_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_tests_choice("include_as_is")
    # )
    # tests_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_tests_choice("exclude_unreliable")
    # )
    # tests_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_tests_choice("flag_improvement")
    # )

    # tests_content = mo.vstack([
    #     mo.md(
    #         "Academic performance metrics from high school and standardised tests (SAT/ACT). "
    #         "Due to test-optional policies implemented during COVID, scores may be missing for many students. "
    #         "Creative solution to transform into a ‘test score submitted’ indicator leverages available information while addressing systematic gaps."
    #     ),
    #     mo.hstack([tests_inc_btn, tests_exc_btn, tests_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Test Scores": tests_content})
    return


@app.cell
def tests_feedback():
    # tests_choice = get_tests_choice()

    # tests_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # tests_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {tests_emoji_map[tests_choice]} **{tests_text_map[tests_choice]}** the variable.")
    return


@app.cell
def tests_justification():
    # tests_selected_flag = get_tests_choice()
    # get_text_just_tests, set_text_just_tests = mo.state("")

    # content_just_tests = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Test Scores choice",
    #         value=get_text_just_tests(),
    #         on_change=lambda v: set_text_just_tests(v),
    #         rows=4,
    #     )
    #     if tests_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_tests
    return


@app.cell
def midterm_status():
    # get_midterm_choice, set_midterm_choice = mo.state(None)

    # midterm_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_midterm_choice("include_as_is")
    # )
    # midterm_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_midterm_choice("exclude_unreliable")
    # )
    # midterm_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_midterm_choice("flag_improvement")
    # )

    # midterm_content = mo.vstack([
    #     mo.md(
    #         "Preliminary academic performance indicators halfway through the term. "
    #         "Identified as valuable but not consistently available across courses."
    #     ),
    #     mo.hstack([midterm_inc_btn, midterm_exc_btn, midterm_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Mid-Term Grades": midterm_content})
    return


@app.cell
def midterm_feedback():
    # midterm_choice = get_midterm_choice()

    # midterm_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # midterm_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {midterm_emoji_map[midterm_choice]} **{midterm_text_map[midterm_choice]}** the variable.")
    return


@app.cell
def midterm_justification():
    # midterm_selected_flag = get_midterm_choice()
    # get_text_just_midterm, set_text_just_midterm = mo.state("")

    # content_just_midterm = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Mid-Term Grades choice",
    #         value=get_text_just_midterm(),
    #         on_change=lambda v: set_text_just_midterm(v),
    #         rows=4,
    #     )
    #     if midterm_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_midterm
    return


@app.cell
def epr_status():
    # get_epr_choice, set_epr_choice = mo.state(None)

    # epr_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_epr_choice("include_as_is")
    # )
    # epr_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_epr_choice("exclude_unreliable")
    # )
    # epr_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_epr_choice("flag_improvement")
    # )

    # epr_content = mo.vstack([
    #     mo.md(
    #         "Faculty-submitted assessments of student performance early in the semester. "
    #         "Reporting inconsistency means this potentially valuable early-warning indicator isn’t reliable enough to include."
    #     ),
    #     mo.hstack([epr_inc_btn, epr_exc_btn, epr_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Early Progress Reports": epr_content})
    return


@app.cell
def epr_feedback():
    # epr_choice = get_epr_choice()

    # epr_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # epr_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {epr_emoji_map[epr_choice]} **{epr_text_map[epr_choice]}** the variable.")
    return


@app.cell
def epr_justification():
    # epr_selected_flag = get_epr_choice()
    # get_text_just_epr, set_text_just_epr = mo.state("")

    # content_just_epr = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Early Progress Reports choice",
    #         value=get_text_just_epr(),
    #         on_change=lambda v: set_text_just_epr(v),
    #         rows=4,
    #     )
    #     if epr_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_epr
    return


@app.cell
def printer_status():
    # get_printer_choice, set_printer_choice = mo.state(None)

    # printer_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_printer_choice("include_as_is")
    # )
    # printer_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_printer_choice("exclude_unreliable")
    # )
    # printer_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_printer_choice("flag_improvement")
    # )

    # printer_content = mo.vstack([
    #     mo.md(
    #         "Weekly count of pages printed in residence-hall printers. "
    #         "Logs are missing whenever printers are offline; many students use personal or library printers instead."
    #     ),
    #     mo.hstack([printer_inc_btn, printer_exc_btn, printer_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Dorm-Printer Usage": printer_content})
    return


@app.cell
def printer_feedback():
    # printer_choice = get_printer_choice()

    # printer_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # printer_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {printer_emoji_map[printer_choice]} **{printer_text_map[printer_choice]}** the variable.")
    return


@app.cell
def printer_justification():
    # printer_selected_flag = get_printer_choice()
    # get_text_just_printer, set_text_just_printer = mo.state("")

    # content_just_printer = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Dorm-Printer Usage choice",
    #         value=get_text_just_printer(),
    #         on_change=lambda v: set_text_just_printer(v),
    #         rows=4,
    #     )
    #     if printer_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_printer
    return


@app.cell
def detailed_feedback_task3():
    # # --- High-School GPA ---
    # hsgpa = get_hsgpa_choice()
    # if hsgpa == "include_as_is":
    #     msg_hsgpa = "High-school GPAs lack standardisation; predictive value may be swamped by noise. Consider excluding or flagging for quality remediation."
    # elif hsgpa == "exclude_unreliable":
    #     msg_hsgpa = "Removing High-School GPA sacrifices a widely used predictor. Could a scaled or percentile version salvage reliability?"
    # elif hsgpa == "flag_improvement":
    #     msg_hsgpa = "Right call"
    # else:
    #     msg_hsgpa = ""

    # # --- Test Scores ---
    # tests = get_tests_choice()
    # if tests == "include_as_is":
    #     msg_tests = "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. A submission indicator or audit flag may be safer."
    # elif tests == "exclude_unreliable":
    #     msg_tests = "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. Could you retain a binary ‘submitted’ flag instead?"
    # elif tests == "flag_improvement":
    #     msg_tests = "Right call"
    # else:
    #     msg_tests = ""

    # # --- Mid-Term Grades ---
    # midterm = get_midterm_choice()
    # if midterm == "include_as_is":
    #     msg_midterm = "Mid-Term Grades appear only for certain courses, risking departmental bias. Flag for quality improvement or exclude."
    # elif midterm == "exclude_unreliable":
    #     msg_midterm = "Excluding Mid-Term Grades forfeits early academic-performance insight. Could selective inclusion or data-quality work make it viable?"
    # elif midterm == "flag_improvement":
    #     msg_midterm = "Right call"
    # else:
    #     msg_midterm = ""

    # # --- Early Progress Reports ---
    # epr = get_epr_choice()
    # if epr == "include_as_is":
    #     msg_epr = "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion."
    # elif epr == "exclude_unreliable":
    #     msg_epr = "You lose a proven early-alert signal. Engage stakeholders to improve reporting rather than discard entirely."
    # elif epr == "flag_improvement":
    #     msg_epr = "Right call"
    # else:
    #     msg_epr = ""

    # # --- Dorm-Printer Usage ---
    # printer = get_printer_choice()
    # if printer == "include_as_is":
    #     msg_printer = "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. Little theoretical link to persistence."
    # elif printer == "flag_improvement":
    #     msg_printer = "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost."
    # elif printer == "exclude_unreliable":
    #     msg_printer = "Appropriate—the variable is weakly linked to retention and suffers systemic gaps."
    # else:
    #     msg_printer = ""

    # content_detail_feedback3 = mo.vstack([
    #     mo.md(f"**High-School GPA:** {msg_hsgpa}"),
    #     mo.md(f"**Test Scores:** {msg_tests}"),
    #     mo.md(f"**Mid-Term Grades:** {msg_midterm}"),
    #     mo.md(f"**Early Progress Reports:** {msg_epr}"),
    #     mo.md(f"**Dorm-Printer Usage:** {msg_printer}"),
    # ])

    # mo.accordion({"Detailed Feedback – Task 3": content_detail_feedback3})
    return


@app.cell
def legacy_status():
    # get_legacy_choice, set_legacy_choice = mo.state(None)

    # legacy_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_legacy_choice("include_as_is")
    # )
    # legacy_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_legacy_choice("exclude_unreliable")
    # )
    # legacy_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_legacy_choice("flag_improvement")
    # )

    # legacy_content = mo.vstack([
    #     mo.md(
    #         "Whether the student has family members who previously attended the university. "
    #         "May indicate stronger institutional ties."
    #     ),
    #     mo.hstack([legacy_inc_btn, legacy_exc_btn, legacy_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Legacy Status": legacy_content})
    return


@app.cell
def legacy_feedback():
    # legacy_choice = get_legacy_choice()

    # legacy_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # legacy_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {legacy_emoji_map[legacy_choice]} **{legacy_text_map[legacy_choice]}** the variable.")
    return


@app.cell
def legacy_justification():
    # legacy_selected_flag = get_legacy_choice()
    # get_text_just_legacy, set_text_just_legacy = mo.state("")

    # content_just_legacy = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Legacy Status choice",
    #         value=get_text_just_legacy(),
    #         on_change=lambda v: set_text_just_legacy(v),
    #         rows=4,
    #     )
    #     if legacy_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_legacy
    return


@app.cell
def athlete_status():
    # get_athlete_choice, set_athlete_choice = mo.state(None)

    # athlete_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_athlete_choice("include_as_is")
    # )
    # athlete_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_athlete_choice("exclude_unreliable")
    # )
    # athlete_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_athlete_choice("flag_improvement")
    # )

    # athlete_content = mo.vstack([
    #     mo.md(
    #         "Whether the student participates in university athletics. May indicate additional support structures but also time commitments."
    #     ),
    #     mo.hstack([athlete_inc_btn, athlete_exc_btn, athlete_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Student Athlete Status": athlete_content})
    return


@app.cell
def athlete_feedback():
    # athlete_choice = get_athlete_choice()

    # athlete_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # athlete_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {athlete_emoji_map[athlete_choice]} **{athlete_text_map[athlete_choice]}** the variable.")
    return


@app.cell
def athlete_justification():
    # athlete_selected_flag = get_athlete_choice()
    # get_text_just_athlete, set_text_just_athlete = mo.state("")

    # content_just_athlete = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Student Athlete Status choice",
    #         value=get_text_just_athlete(),
    #         on_change=lambda v: set_text_just_athlete(v),
    #         rows=4,
    #     )
    #     if athlete_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_athlete
    return


@app.cell
def firstgen_status():
    # get_firstgen_choice, set_firstgen_choice = mo.state(None)

    # firstgen_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_firstgen_choice("include_as_is")
    # )
    # firstgen_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_firstgen_choice("exclude_unreliable")
    # )
    # firstgen_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_firstgen_choice("flag_improvement")
    # )

    # firstgen_content = mo.vstack([
    #     mo.md(
    #         "Indicates if the student is the first in their family to attend college; may reflect differences in familiarity with college processes."
    #     ),
    #     mo.hstack([firstgen_inc_btn, firstgen_exc_btn, firstgen_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"First-Generation Student": firstgen_content})
    return


@app.cell
def firstgen_feedback():
    # firstgen_choice = get_firstgen_choice()

    # firstgen_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # firstgen_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {firstgen_emoji_map[firstgen_choice]} **{firstgen_text_map[firstgen_choice]}** the variable.")
    return


@app.cell
def firstgen_justification():
    # firstgen_selected_flag = get_firstgen_choice()
    # get_text_just_firstgen, set_text_just_firstgen = mo.state("")

    # content_just_firstgen = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your First-Generation Student choice",
    #         value=get_text_just_firstgen(),
    #         on_change=lambda v: set_text_just_firstgen(v),
    #         rows=4,
    #     )
    #     if firstgen_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_firstgen
    return


@app.cell
def distance_status():
    # get_distance_choice, set_distance_choice = mo.state(None)

    # distance_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_distance_choice("include_as_is")
    # )
    # distance_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_distance_choice("exclude_unreliable")
    # )
    # distance_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_distance_choice("flag_improvement")
    # )

    # distance_content = mo.vstack([
    #     mo.md(
    #         "Calculated metric based on student’s home address and campus location; privacy-preserving alternative to ZIP codes."
    #     ),
    #     mo.hstack([distance_inc_btn, distance_exc_btn, distance_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Distance from Home": distance_content})
    return


@app.cell
def distance_feedback():
    # distance_choice = get_distance_choice()

    # distance_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # distance_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {distance_emoji_map[distance_choice]} **{distance_text_map[distance_choice]}** the variable.")
    return


@app.cell
def distance_justification():
    # distance_selected_flag = get_distance_choice()
    # get_text_just_distance, set_text_just_distance = mo.state("")

    # content_just_distance = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Distance from Home choice",
    #         value=get_text_just_distance(),
    #         on_change=lambda v: set_text_just_distance(v),
    #         rows=4,
    #     )
    #     if distance_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_distance
    return


@app.cell
def credits_status():
    # get_credits_choice, set_credits_choice = mo.state(None)

    # credits_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_credits_choice("include_as_is")
    # )
    # credits_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_credits_choice("exclude_unreliable")
    # )
    # credits_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_credits_choice("flag_improvement")
    # )

    # credits_content = mo.vstack([
    #     mo.md(
    #         "Credit hours the student is taking after the official add/drop deadline; may reflect adjustment to academic realities."
    #     ),
    #     mo.hstack([credits_inc_btn, credits_exc_btn, credits_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Credits After Add/Drop": credits_content})
    return


@app.cell
def credits_feedback():
    # credits_choice = get_credits_choice()

    # credits_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # credits_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {credits_emoji_map[credits_choice]} **{credits_text_map[credits_choice]}** the variable.")
    return


@app.cell
def credits_justification():
    # credits_selected_flag = get_credits_choice()
    # get_text_just_credits, set_text_just_credits = mo.state("")

    # content_just_credits = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Credits After Add/Drop choice",
    #         value=get_text_just_credits(),
    #         on_change=lambda v: set_text_just_credits(v),
    #         rows=4,
    #     )
    #     if credits_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_credits
    return


@app.cell
def livecampus_status():
    # get_livecampus_choice, set_livecampus_choice = mo.state(None)

    # livecampus_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_livecampus_choice("include_as_is")
    # )
    # livecampus_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_livecampus_choice("exclude_unreliable")
    # )
    # livecampus_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_livecampus_choice("flag_improvement")
    # )

    # livecampus_content = mo.vstack([
    #     mo.md(
    #         "Housing status affects integration into campus life and access to resources."
    #     ),
    #     mo.hstack([livecampus_inc_btn, livecampus_exc_btn, livecampus_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Live On-Campus or Commuter": livecampus_content})
    return


@app.cell
def livecampus_feedback():
    # livecampus_choice = get_livecampus_choice()

    # livecampus_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # livecampus_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {livecampus_emoji_map[livecampus_choice]} **{livecampus_text_map[livecampus_choice]}** the variable.")
    return


@app.cell
def livecampus_justification():
    # livecampus_selected_flag = get_livecampus_choice()
    # get_text_just_livecampus, set_text_just_livecampus = mo.state("")

    # content_just_livecampus = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Live On-Campus or Commuter choice",
    #         value=get_text_just_livecampus(),
    #         on_change=lambda v: set_text_just_livecampus(v),
    #         rows=4,
    #     )
    #     if livecampus_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_livecampus
    return


@app.cell
def residency_status():
    # get_residency_choice, set_residency_choice = mo.state(None)

    # residency_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_residency_choice("include_as_is")
    # )
    # residency_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_residency_choice("exclude_unreliable")
    # )
    # residency_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_residency_choice("flag_improvement")
    # )

    # residency_content = mo.vstack([
    #     mo.md(
    #         "Affects tuition rates and connection to campus."
    #     ),
    #     mo.hstack([residency_inc_btn, residency_exc_btn, residency_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Residency (In-State / Out-of-State / International)": residency_content})
    return


@app.cell
def residency_feedback():
    # residency_choice = get_residency_choice()

    # residency_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # residency_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {residency_emoji_map[residency_choice]} **{residency_text_map[residency_choice]}** the variable.")
    return


@app.cell
def residency_justification():
    # 
    return


@app.cell
def origin_status():
    # get_origin_choice, set_origin_choice = mo.state(None)

    # origin_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_origin_choice("include_as_is")
    # )
    # origin_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_origin_choice("exclude_unreliable")
    # )
    # origin_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_origin_choice("flag_improvement")
    # )

    # origin_content = mo.vstack([
    #     mo.md(
    #         "Classification of student’s home community; derived from heuristics."
    #     ),
    #     mo.hstack([origin_inc_btn, origin_exc_btn, origin_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Urban / Rural / Suburban Origin": origin_content})
    return


@app.cell
def origin_feedback():
    # origin_choice = get_origin_choice()

    # origin_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # origin_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {origin_emoji_map[origin_choice]} **{origin_text_map[origin_choice]}** the variable.")
    return


@app.cell
def origin_justification():
    # origin_selected_flag = get_origin_choice()
    # get_text_just_origin, set_text_just_origin = mo.state("")

    # content_just_origin = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Urban / Rural / Suburban Origin choice",
    #         value=get_text_just_origin(),
    #         on_change=lambda v: set_text_just_origin(v),
    #         rows=4,
    #     )
    #     if origin_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_origin
    return


@app.cell
def transfer_status():
    # get_transfer_choice, set_transfer_choice = mo.state(None)

    # transfer_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_transfer_choice("include_as_is")
    # )
    # transfer_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_transfer_choice("exclude_unreliable")
    # )
    # transfer_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_transfer_choice("flag_improvement")
    # )

    # transfer_content = mo.vstack([
    #     mo.md(
    #         "Whether the student transferred from another institution versus starting as a first-year."
    #     ),
    #     mo.hstack([transfer_inc_btn, transfer_exc_btn, transfer_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Transfer Status": transfer_content})
    return


@app.cell
def transfer_feedback():
    # transfer_choice = get_transfer_choice()

    # transfer_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # transfer_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {transfer_emoji_map[transfer_choice]} **{transfer_text_map[transfer_choice]}** the variable.")
    return


@app.cell
def transfer_justification():
    # transfer_selected_flag = get_transfer_choice()
    # get_text_just_transfer, set_text_just_transfer = mo.state("")

    # content_just_transfer = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Transfer Status choice",
    #         value=get_text_just_transfer(),
    #         on_change=lambda v: set_text_just_transfer(v),
    #         rows=4,
    #     )
    #     if transfer_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_transfer
    return


@app.cell
def extracurricular_status():
    # get_extracurricular_choice, set_extracurricular_choice = mo.state(None)

    # extracurricular_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_extracurricular_choice("include_as_is")
    # )
    # extracurricular_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_extracurricular_choice("exclude_unreliable")
    # )
    # extracurricular_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_extracurricular_choice("flag_improvement")
    # )

    # extracurricular_content = mo.vstack([
    #     mo.md(
    #         "Participation in clubs or other non-academic activities; data collection relies on self-reporting."
    #     ),
    #     mo.hstack([extracurricular_inc_btn, extracurricular_exc_btn, extracurricular_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Extracurricular Involvement": extracurricular_content})
    return


@app.cell
def extracurricular_feedback():
    # extracurricular_choice = get_extracurricular_choice()

    # extracurricular_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # extracurricular_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {extracurricular_emoji_map[extracurricular_choice]} **{extracurricular_text_map[extracurricular_choice]}** the variable.")
    return


@app.cell
def extracurricular_justification():
    # extracurricular_selected_flag = get_extracurricular_choice()
    # get_text_just_extracurricular, set_text_just_extracurricular = mo.state("")

    # content_just_extracurricular = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Extracurricular Involvement choice",
    #         value=get_text_just_extracurricular(),
    #         on_change=lambda v: set_text_just_extracurricular(v),
    #         rows=4,
    #     )
    #     if extracurricular_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_extracurricular
    return


@app.cell
def gaming_status():
    # get_gaming_choice, set_gaming_choice = mo.state(None)

    # gaming_inc_btn = mo.ui.button(
    #     label="Include as-is", kind="success", on_click=lambda _: set_gaming_choice("include_as_is")
    # )
    # gaming_exc_btn = mo.ui.button(
    #     label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_gaming_choice("exclude_unreliable")
    # )
    # gaming_flag_btn = mo.ui.button(
    #     label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_gaming_choice("flag_improvement")
    # )

    # gaming_content = mo.vstack([
    #     mo.md(
    #         "Binary flag—student devices connected to high-traffic gaming ports for ≥ 5 hours/week during evenings."
    #     ),
    #     mo.hstack([gaming_inc_btn, gaming_exc_btn, gaming_flag_btn], gap="1rem"),
    # ])
    # mo.accordion({"Campus-Wi-Fi Gaming Network Participation": gaming_content})
    return


@app.cell
def gaming_feedback():
    # gaming_choice = get_gaming_choice()

    # gaming_emoji_map = {
    #     "include_as_is": "🟢",
    #     "exclude_unreliable": "🔴",
    #     "flag_improvement": "🟠",
    #     None: "⚪️",
    # }
    # gaming_text_map = {
    #     "include_as_is": "Include as-is",
    #     "exclude_unreliable": "Exclude (too unreliable)",
    #     "flag_improvement": "Flag for Data-Quality Improvement",
    #     None: "no selection",
    # }

    # mo.md(f"You decided to {gaming_emoji_map[gaming_choice]} **{gaming_text_map[gaming_choice]}** the variable.")
    return


@app.cell
def gaming_justification():
    # gaming_selected_flag = get_gaming_choice()
    # get_text_just_gaming, set_text_just_gaming = mo.state("")

    # content_just_gaming = (
    #     mo.ui.text_area(
    #         label="Please briefly justify your reasoning for your Campus-Wi-Fi Gaming choice",
    #         value=get_text_just_gaming(),
    #         on_change=lambda v: set_text_just_gaming(v),
    #         rows=4,
    #     )
    #     if gaming_selected_flag is not None
    #     else mo.md("")
    # )
    # content_just_gaming
    return


@app.cell
def detailed_feedback_task4():
    # # --- Legacy Status ---
    # legacy = get_legacy_choice()
    # if legacy == "include_as_is":
    #     msg_legacy = "Legacy Status may encode privilege and could unfairly prioritise well-connected students. Document why its predictive gain outweighs equity concerns."
    # elif legacy == "exclude_unreliable":
    #     msg_legacy = "You removed a factor linked to institutional attachment. Could advisors design fair interventions if they knew a student lacked legacy ties?"
    # elif legacy == "flag_improvement":
    #     msg_legacy = "Right call"
    # else:
    #     msg_legacy = ""

    # # --- Student Athlete Status ---
    # athlete = get_athlete_choice()
    # if athlete == "include_as_is":
    #     msg_athlete = "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. Ensure interventions add value."
    # elif athlete == "exclude_unreliable":
    #     msg_athlete = "Athletes juggle academics and sport travel. Excluding this variable may hide a known risk group lacking time for coursework."
    # elif athlete == "flag_improvement":
    #     msg_athlete = "Right call"
    # else:
    #     msg_athlete = ""

    # # --- First-Generation Student ---
    # firstgen = get_firstgen_choice()
    # if firstgen == "include_as_is":
    #     msg_firstgen = "Good call—first-gen status supports equity-minded outreach. Be sure to explain positive, not deficit-based, interventions."
    # elif firstgen == "exclude_unreliable":
    #     msg_firstgen = "First-generation students often benefit from navigational support. Omitting this variable could undermine equity goals."
    # elif firstgen == "flag_improvement":
    #     msg_firstgen = "Right call"
    # else:
    #     msg_firstgen = ""

    # # --- Distance from Home ---
    # distance = get_distance_choice()
    # if distance == "include_as_is":
    #     msg_distance = "Distance correlates with homesickness and travel cost but offers limited intervention levers. Note whether actionable support exists (e.g., travel grants)."
    # elif distance == "exclude_unreliable":
    #     msg_distance = "Ignoring Distance removes insight into geographically isolated students who may need community-building initiatives."
    # elif distance == "flag_improvement":
    #     msg_distance = "Right call"
    # else:
    #     msg_distance = ""

    # # --- Credits After Add/Drop ---
    # credits = get_credits_choice()
    # if credits == "include_as_is":
    #     msg_credits = "Strong early signal of load management issues. Advisors can act quickly—solid choice."
    # elif credits == "exclude_unreliable":
    #     msg_credits = "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value."
    # elif credits == "flag_improvement":
    #     msg_credits = "Right call"
    # else:
    #     msg_credits = ""

    # # --- Live On-Campus or Commuter ---
    # livecampus = get_livecampus_choice()
    # if livecampus == "include_as_is":
    #     msg_livecampus = "Useful and actionable—commuters may need remote-friendly support. Ensure interventions respect time and travel constraints."
    # elif livecampus == "exclude_unreliable":
    #     msg_livecampus = "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk."
    # elif livecampus == "flag_improvement":
    #     msg_livecampus = "Right call"
    # else:
    #     msg_livecampus = ""

    # # --- Residency ---
    # residency = get_residency_choice()
    # if residency == "include_as_is":
    #     msg_residency = "Residency drives cost burden; interventions must avoid stereotyping out-of-state students as less committed."
    # elif residency == "exclude_unreliable":
    #     msg_residency = "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups."
    # elif residency == "flag_improvement":
    #     msg_residency = "Right call"
    # else:
    #     msg_residency = ""

    # # --- Urban / Rural / Suburban Origin ---
    # origin = get_origin_choice()
    # if origin == "include_as_is":
    #     msg_origin = "Heuristic classification may mislabel students; validate definitions or risk noisy signals."
    # elif origin == "exclude_unreliable":
    #     msg_origin = "Campus adjustment often differs by origin. Excluding could overlook rural-to-urban transition challenges."
    # elif origin == "flag_improvement":
    #     msg_origin = "Right call"
    # else:
    #     msg_origin = ""

    # # --- Transfer Status ---
    # transfer = get_transfer_choice()
    # if transfer == "include_as_is":
    #     msg_transfer = "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant."
    # elif transfer == "exclude_unreliable":
    #     msg_transfer = "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support."
    # elif transfer == "flag_improvement":
    #     msg_transfer = "Right call"
    # else:
    #     msg_transfer = ""

    # # --- Extracurricular Involvement ---
    # extracurricular = get_extracurricular_choice()
    # if extracurricular == "include_as_is":
    #     msg_extracurricular = "Self-report bias and missingness limit reliability; document caveats to avoid overstating predictive value."
    # elif extracurricular == "exclude_unreliable":
    #     msg_extracurricular = "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright."
    # elif extracurricular == "flag_improvement":
    #     msg_extracurricular = "Right call"
    # else:
    #     msg_extracurricular = ""

    # # --- Campus-Wi-Fi Gaming Network Participation ---
    # gaming = get_gaming_choice()
    # if gaming == "include_as_is":
    #     msg_gaming = "Correlation to retention unproven; risk of pathologising hobby behaviour. Provide theoretical justification or exclude."
    # elif gaming == "exclude_unreliable":
    #     msg_gaming = "Sensible—no established link to academic persistence."
    # elif gaming == "flag_improvement":
    #     msg_gaming = "Right call"
    # else:
    #     msg_gaming = ""

    # # --- Build accordion content ---
    # content_detail_feedback4 = mo.vstack([
    #     mo.md(f"**Legacy Status:** {msg_legacy}"),
    #     mo.md(f"**Student Athlete Status:** {msg_athlete}"),
    #     mo.md(f"**First-Generation Student:** {msg_firstgen}"),
    #     mo.md(f"**Distance from Home:** {msg_distance}"),
    #     mo.md(f"**Credits After Add/Drop:** {msg_credits}"),
    #     mo.md(f"**Live On-Campus or Commuter:** {msg_livecampus}"),
    #     mo.md(f"**Residency:** {msg_residency}"),
    #     mo.md(f"**Urban / Rural / Suburban Origin:** {msg_origin}"),
    #     mo.md(f"**Transfer Status:** {msg_transfer}"),
    #     mo.md(f"**Extracurricular Involvement:** {msg_extracurricular}"),
    #     mo.md(f"**Campus-Wi-Fi Gaming Network Participation:** {msg_gaming}"),
    # ])

    # mo.accordion({"Detailed Feedback – Task 4": content_detail_feedback4})
    return


@app.cell
def _():
    # # ---- Global submit state ----
    # submit_state, set_submit_state = mo.state(False)

    # # ---- Helper to standardize decision ----
    # def dec_label(choice):
    #     if choice in ["include", "include_as_is"]:
    #         return "Include"
    #     elif choice in ["flag", "flag_improvement", "audit_only"]:
    #         return "Flag"
    #     elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
    #         return "Exclude"
    #     else:
    #         return "No Selection"

    # # ---- Collect all choices ----
    # # all_choices = [
    # #     get_choice(), get_efc_choice(), get_sai_choice(), get_unmet_choice(), get_merit_choice(), get_pplus_choice(),
    # #     get_race_choice(), get_gender_choice(), get_age_choice(), get_pronouns_choice(),
    # #     get_hsgpa_choice(), get_tests_choice(), get_midterm_choice(), get_epr_choice(), get_printer_choice(),
    # #     get_legacy_choice(), get_athlete_choice(), get_firstgen_choice(), get_distance_choice(), get_credits_choice(),
    # #     get_livecampus_choice(), get_residency_choice(), get_origin_choice(), get_transfer_choice(),
    # #     get_extracurricular_choice(), get_gaming_choice()
    # # ]

    # # ---- Count included variables ----
    # include_count = sum(1 for c in all_choices if dec_label(c) == "Include")

    # # ---- Keep returning states for later use ----
    return


@app.cell
def _():

    # def decision_label(choice):
    #     if choice in ["include", "include_as_is", "include_as-is"]:
    #         return "Include"
    #     elif choice in ["flag", "flag_improvement", "audit_only"]:
    #         return "Flag"
    #     elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
    #         return "Exclude"
    #     else:
    #         return "No Selection"

    # grouped_rows




    # grouped_rows = {
    #     "Regulatory Gate": [
    #         (decision_label(get_choice()), "Pell Status"),
    #         (decision_label(get_efc_choice()), "Expected Family Contribution (EFC)"),
    #         (decision_label(get_sai_choice()), "Student Aid Index (SAI)"),
    #         (decision_label(get_unmet_choice()), "Unmet Need"),
    #         (decision_label(get_merit_choice()), "Merit Award Amount"),
    #         (decision_label(get_pplus_choice()), "Pell Plus"),
    #     ],
    #     "Protected-Attribute Gate": [
    #         (decision_label(get_race_choice()), "Race"),
    #         (decision_label(get_gender_choice()), "Gender"),
    #         (decision_label(get_age_choice()), "Age"),
    #         (decision_label(get_pronouns_choice()), "Preferred Pronouns"),
    #     ],
    #     "Data-Reliability Gate": [
    #         (decision_label(get_hsgpa_choice()), "High-School GPA"),
    #         (decision_label(get_tests_choice()), "Test Scores"),
    #         (decision_label(get_midterm_choice()), "Mid-Term Grades"),
    #         (decision_label(get_epr_choice()), "Early Progress Reports"),
    #         (decision_label(get_printer_choice()), "Dorm-Printer Usage"),
    #     ],
    #     "Equity & Actionability Gate": [
    #         (decision_label(get_legacy_choice()), "Legacy Status"),
    #         (decision_label(get_athlete_choice()), "Student Athlete Status"),
    #         (decision_label(get_firstgen_choice()), "First-Generation Student"),
    #         (decision_label(get_distance_choice()), "Distance from Home"),
    #         (decision_label(get_credits_choice()), "Credits After Add/Drop"),
    #         (decision_label(get_livecampus_choice()), "Live On-Campus or Commuter"),
    #         (decision_label(get_residency_choice()), "Residency (In/Out/International)"),
    #         (decision_label(get_origin_choice()), "Urban / Rural / Suburban Origin"),
    #         (decision_label(get_transfer_choice()), "Transfer Status"),
    #         (decision_label(get_extracurricular_choice()), "Extracurricular Involvement"),
    #         (decision_label(get_gaming_choice()), "Campus-Wi-Fi Gaming Participation"),
    #     ],
    # }

    # # build table HTML
    # table_html = "<table style='border-collapse:collapse; width:100%; text-align:left;'>"
    # table_html += "<thead><tr><th>Group (Wave)</th><th>Decision</th><th>Variable</th></tr></thead><tbody>"

    # for group, rows in grouped_rows.items():
    #     # group header row
    #     table_html += f"<tr><td colspan='3' style='font-weight:bold; padding-top:10px;'>{group}</td></tr>"
    #     # variable rows
    #     for decision, variable in rows:
    #         color = " style='background-color:#e8f5e9;'" if decision == "Include" else ""
    #         table_html += f"<tr{color}><td></td><td>{decision}</td><td>{variable}</td></tr>"
    #     # blank line between groups
    #     table_html += "<tr><td colspan='3' style='height:8px;'></td></tr>"

    # table_html += "</tbody></table>"

    # mo.vstack([
    #     mo.md("## End-of-Scenario Wrap-Up – Variable-Selection Brief"),
    #     mo.md(
    #     f"**_Your model will use the {include_count} variables highlighted in green._** "
    #     "Is this acceptable, or would you like to revise your selections?"
    # ),
    #     mo.Html(table_html)
    # ])
    return


@app.cell
def wrapup_buttons():
    # buttons_html = f"""
    #     <a href="#task_1>
    #         Review Wave 1
    #     </a>
    #     # <a href="#task_2" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
    #     #     Review Wave 2
    #     # </a>
    #     # <a href="#task_3" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
    #     #     Review Wave 3
    #     # </a>
    #     # <a href="#task_4" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
    #     #     Review Wave 4
    #     # </a>
    # """

    # # Thick horizontal line + centered light green title
    # final_feedback_html = f"""
    # <hr style="border: 3px solid #4CAF50; margin-top:1rem; margin-bottom:1rem;">
    # <div style="text-align:center; color:#4CAF50; font-size:1.5rem; font-weight:bold; margin-bottom:1rem;">
    #     Final Feedback
    # </div>
    # """

    # # mo.output.replace(mo.vstack([
    # # mo.Html(buttons_html),
    # # mo.Html(final_feedback_html)
    # # ]))

    # mo.Html(buttons_html)
    return


@app.cell
def wrapup_feedback_regulatory():
    # def feedback_text(var, sel):
    #     if var == "Pell Status":
    #         if sel == "include":
    #             return "Including Pell Status violates current federal guidance and may expose the institution to penalties. Consider aggregate reporting instead of individual-level use."
    #         elif sel in ["flag", "exclude"]:
    #             return "Right call"
    #     elif var == "Expected Family Contribution (EFC)":
    #         if sel == "include":
    #             return "EFC is explicitly barred under 2024 Department of Education rules; its inclusion would render the model non-compliant."
    #         elif sel in ["flag", "exclude"]:
    #             return "Right call"
    #     elif var == "Student Aid Index (SAI)":
    #         if sel == "include":
    #             return "SAI is sensitive financial-aid data with incomplete coverage. Using it risks privacy violations and injects missing-data bias."
    #         elif sel in ["flag", "exclude"]:
    #             return "Right call"
    #     elif var == "Unmet Need":
    #         if sel == "include":
    #             return "Unmet Need combines multiple restricted data points. Including it would contravene policy and amplify socioeconomic bias."
    #         elif sel in ["flag", "exclude"]:
    #             return "Right call"
    #     elif var == "Merit Award Amount":
    #         if sel == "include":
    #             return "Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. Use only with a strong equity justification."
    #         elif sel in ["flag", "exclude"]:
    #             return "Right call"
    #     elif var == "Pell Plus":
    #         if sel == "include":
    #             return "Pell Plus directly signals Pell participation; individual-level use is restricted. Exclude or seek explicit legal clearance."
    #         elif sel in ["flag", "exclude"]:
    #             return "Right call"

    # vars_choices = {
    #     "Pell Status": get_pell_state(),
    #     "Expected Family Contribution (EFC)": get_efc_state(),
    #     "Student Aid Index (SAI)": get_sai_state(),
    #     "Unmet Need": get_unmet_state(),
    #     "Merit Award Amount": get_merit_state(),
    #     "Pell Plus": get_pell_plus_state(),
    # }

    # alert_flag = False
    # wrong_lines = []
    # correct_vars = []

    # for var, sel in vars_choices.items():
    #     txt = feedback_text(var, sel)
    #     if txt and "Right call" not in txt:
    #         alert_flag = True
    #         wrong_lines.append(mo.md(f"**{var}:** {txt}"))
    #     else:
    #         correct_vars.append(var)

    # # wave-level alert
    # wave_alert = (
    #     mo.md("⚠️ **At least one restricted variable still needs your attention.**")
    #     if alert_flag else
    #     mo.md("✅ **Everything looks good in this wave!**")
    # )

    # correct_line = (
    #     mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars)}")
    #     if correct_vars else mo.md("")
    # )

    # mo.accordion(
    #     {"Regulatory Gate Feedback": mo.vstack([wave_alert] + wrong_lines + [correct_line])}
    # )
    return


@app.cell
def wrapup_feedback_protected():
    # # --- Helper to compare correct vs wrong ---
    # def feedback_text_protected(var_protected, choice_protected):
    #     if var_protected == "Race":
    #         if choice_protected == "include_as_is":
    #             return "Using Race as a predictive feature can embed historical inequities and violate institutional policy. Retain only for bias-audit."
    #         elif choice_protected == "exclude_entirely":
    #             return "Without Race you lose the ability to audit fair outcomes across groups. Best practice is to keep it for auditing while excluding it from model training."
    #         elif choice_protected == "audit_only":
    #             return "Right call"

    #     elif var_protected == "Gender":
    #         if choice_protected == "include_as_is":
    #             return "Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention."
    #         elif choice_protected == "exclude_entirely":
    #             return "Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs."
    #         elif choice_protected == "audit_only":
    #             return "Right call"

    #     elif var_protected == "Age":
    #         if choice_protected == "include_as_is":
    #             return "Age may correlate with persistence but also with protected status (non-traditional learners). Document equity safeguards or shift to audit-only use."
    #         elif choice_protected == "exclude_entirely":
    #             return "Excluding Age erases patterns relevant to adult learners and hampers fairness checks. Audit-only use is often a balanced choice."
    #         elif choice_protected == "audit_only":
    #             return "Right call"

    #     elif var_protected == "Preferred Pronouns":
    #         if choice_protected == "include_as_is":
    #             return "Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. Exclude or store only for awareness training, not analytics."
    #         elif choice_protected == "audit_only":
    #             return "Pronoun data lack completeness and standardization, limiting audit utility. Exclusion is usually appropriate."
    #         elif choice_protected == "exclude_entirely":
    #             return "Right call"

    # # build feedback lines
    # wrong_lines_protected = []
    # correct_vars_protected = []
    # alert_flag_protected = False

    # vars_choices_protected = {
    #     "Race": get_race_choice(),
    #     "Gender": get_gender_choice(),
    #     "Age": get_age_choice(),
    #     "Preferred Pronouns": get_pronouns_choice(),
    # }

    # for var_protected, choice_protected in vars_choices_protected.items():
    #     txt_protected = feedback_text_protected(var_protected, choice_protected)
    #     if txt_protected and "Right call" not in txt_protected:
    #         alert_flag_protected = True
    #         wrong_lines_protected.append(mo.md(f"**{var_protected}:** {txt_protected}"))
    #     else:
    #         correct_vars_protected.append(var_protected)

    # # wave-level alert
    # wave_alert_protected = (
    #     mo.md("⚠️ **At least one restricted variable still needs your attention.**")
    #     if alert_flag_protected else
    #     mo.md("✅ **Everything looks good in this wave!**")
    # )

    # correct_line_protected = (
    #     mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars_protected)}")
    #     if correct_vars_protected else mo.md("")
    # )

    # mo.accordion({
    #     "Protected-Attribute Gate Feedback": mo.vstack(
    #         [wave_alert_protected] + wrong_lines_protected + [correct_line_protected]
    #     )
    # })
    return


@app.cell
def wrapup_feedback_reliability():
    # # --- Helper to compare correct vs wrong ---
    # def feedback_text_reliability(var_reliability, choice_reliability):
    #     if var_reliability == "High-School GPA":
    #         if choice_reliability == "include_as_is":
    #             return "High-school GPAs lack standardisation; predictive value may be swamped by noise. Consider excluding or flagging for quality remediation."
    #         elif choice_reliability == "exclude_unreliable":
    #             return "Right call"
    #         elif choice_reliability == "flag_improvement":
    #             return "Right call"
    #     elif var_reliability == "Test Scores":
    #         if choice_reliability == "include_as_is":
    #             return "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. A submission indicator or audit flag may be safer."
    #         elif choice_reliability == "exclude_unreliable":
    #             return "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. Could you retain a binary ‘submitted’ flag instead?"
    #         elif choice_reliability == "flag_improvement":
    #             return "Right call"
    #     elif var_reliability == "Mid-Term Grades":
    #         if choice_reliability == "include_as_is":
    #             return "Mid-Term Grades appear only for certain courses, risking departmental bias. Flag for quality improvement or exclude."
    #         elif choice_reliability == "exclude_unreliable":
    #             return "Excluding Mid-Term Grades forfeits early academic-performance insight. Could selective inclusion or data-quality work make it viable?"
    #         elif choice_reliability == "flag_improvement":
    #             return "Right call"

    #     elif var_reliability == "Early Progress Reports":
    #         if choice_reliability == "include_as_is":
    #             return "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion."
    #         elif choice_reliability == "exclude_unreliable":
    #             return "You lose a proven early-alert signal. Engage stakeholders to improve reporting rather than discard entirely."
    #         elif choice_reliability == "flag_improvement":
    #             return "Right call"

    #     elif var_reliability == "Dorm-Printer Usage":
    #         if choice_reliability == "include_as_is":
    #             return "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. Little theoretical link to persistence."
    #         elif choice_reliability == "flag_improvement":
    #             return "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost."
    #         elif choice_reliability == "exclude_unreliable":
    #             return "Right call"

    # # build feedback lines
    # wrong_lines_reliability = []
    # correct_vars_reliability = []
    # alert_flag_reliability = False

    # vars_choices_reliability = {
    #     "High-School GPA": get_hsgpa_choice(),
    #     "Test Scores": get_tests_choice(),
    #     "Mid-Term Grades": get_midterm_choice(),
    #     "Early Progress Reports": get_epr_choice(),
    #     "Dorm-Printer Usage": get_printer_choice(),
    # }

    # for var_reliability, choice_reliability in vars_choices_reliability.items():
    #     txt_reliability = feedback_text_reliability(var_reliability, choice_reliability)
    #     if txt_reliability and "Right call" not in txt_reliability:
    #         alert_flag_reliability = True
    #         wrong_lines_reliability.append(mo.md(f"**{var_reliability}:** {txt_reliability}"))
    #     else:
    #         correct_vars_reliability.append(var_reliability)

    # wave_alert_reliability = (
    #     mo.md("⚠️ **At least one restricted variable still needs your attention.**")
    #     if alert_flag_reliability else
    #     mo.md("✅ **Everything looks good in this wave!**")
    # )

    # correct_line_reliability = (
    #     mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars_reliability)}")
    #     if correct_vars_reliability else mo.md("")
    # )

    # mo.accordion({
    #     "Data-Reliability Gate Feedback": mo.vstack(
    #         [wave_alert_reliability] + wrong_lines_reliability + [correct_line_reliability]
    #     )
    # })
    return


@app.cell
def wrapup_feedback_equity():
    # # --- Helper to compare correct vs wrong ---
    # def feedback_text_equity(var_equity, choice_equity):
    #     if var_equity == "Legacy Status":
    #         if choice_equity == "include_as_is":
    #             return "Legacy Status may encode privilege and could unfairly prioritise well-connected students. Document why its predictive gain outweighs equity concerns."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Right call"
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Student Athlete Status":
    #         if choice_equity == "include_as_is":
    #             return "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. Ensure interventions add value."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Athletes juggle academics and sport travel. Excluding this variable may hide a known risk group lacking time for coursework."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "First-Generation Student":
    #         if choice_equity == "include_as_is":
    #             return "Good call—first-gen status supports equity-minded outreach. Be sure to explain positive, not deficit-based, interventions."
    #         elif choice_equity == "exclude_unreliable":
    #             return "First-generation students often benefit from navigational support. Omitting this variable could undermine equity goals."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Distance from Home":
    #         if choice_equity == "include_as_is":
    #             return "Distance correlates with homesickness and travel cost but offers limited intervention levers. Note whether actionable support exists (e.g., travel grants)."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Ignoring Distance removes insight into geographically isolated students who may need community-building initiatives."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Credits After Add/Drop":
    #         if choice_equity == "include_as_is":
    #             return "Strong early signal of load management issues. Advisors can act quickly—solid choice."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Live On-Campus or Commuter":
    #         if choice_equity == "include_as_is":
    #             return "Useful and actionable—commuters may need remote-friendly support. Ensure interventions respect time and travel constraints."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Residency (In-State / Out-of-State / International)":
    #         if choice_equity == "include_as_is":
    #             return "Residency drives cost burden; interventions must avoid stereotyping out-of-state students as less committed."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Urban / Rural / Suburban Origin":
    #         if choice_equity == "include_as_is":
    #             return "Heuristic classification may mislabel students; validate definitions or risk noisy signals."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Campus adjustment often differs by origin. Excluding could overlook rural-to-urban transition challenges."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Transfer Status":
    #         if choice_equity == "include_as_is":
    #             return "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant."
    #         elif choice_equity == "exclude_unreliable":
    #             return "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Extracurricular Involvement":
    #         if choice_equity == "include_as_is":
    #             return "Self-report bias and missingness limit reliability; document caveats to avoid overstating predictive value."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright."
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    #     elif var_equity == "Campus-Wi-Fi Gaming Network Participation":
    #         if choice_equity == "include_as_is":
    #             return "Correlation to retention unproven; risk of pathologising hobby behaviour. Provide theoretical justification or exclude."
    #         elif choice_equity == "exclude_unreliable":
    #             return "Right call"
    #         elif choice_equity == "flag_improvement":
    #             return "Right call"

    # # build feedback lines
    # wrong_lines_equity = []
    # correct_vars_equity = []
    # alert_flag_equity = False

    # vars_choices_equity = {
    #     "Legacy Status": get_legacy_choice(),
    #     "Student Athlete Status": get_athlete_choice(),
    #     "First-Generation Student": get_firstgen_choice(),
    #     "Distance from Home": get_distance_choice(),
    #     "Credits After Add/Drop": get_credits_choice(),
    #     "Live On-Campus or Commuter": get_livecampus_choice(),
    #     "Residency (In-State / Out-of-State / International)": get_residency_choice(),
    #     "Urban / Rural / Suburban Origin": get_origin_choice(),
    #     "Transfer Status": get_transfer_choice(),
    #     "Extracurricular Involvement": get_extracurricular_choice(),
    #     "Campus-Wi-Fi Gaming Network Participation": get_gaming_choice(),
    # }

    # for var_equity, choice_equity in vars_choices_equity.items():
    #     txt_equity = feedback_text_equity(var_equity, choice_equity)
    #     if txt_equity and "Right call" not in txt_equity:
    #         alert_flag_equity = True
    #         wrong_lines_equity.append(mo.md(f"**{var_equity}:** {txt_equity}"))
    #     else:
    #         correct_vars_equity.append(var_equity)

    # wave_alert_equity = (
    #     mo.md("⚠️ **At least one restricted variable still needs your attention.**")
    #     if alert_flag_equity else
    #     mo.md("✅ **Everything looks good in this wave!**")
    # )

    # correct_line_equity = (
    #     mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars_equity)}")
    #     if correct_vars_equity else mo.md("")
    # )

    # mo.accordion({
    #     "Equity & Actionability Gate Feedback": mo.vstack(
    #         [wave_alert_equity] + wrong_lines_equity + [correct_line_equity]
    #     )
    # })
    return


if __name__ == "__main__":
    app.run()
