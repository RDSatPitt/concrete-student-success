
import marimo                                     
app = marimo.App(width="medium")

@app.cell
def _():
    import marimo as mo                           
    mo.md(
        "# Variable selection scenario\n"
        
    )


# ------------------------------------------------------------
# Task 1
# ------------------------------------------------------------

@app.cell
def task_1():
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

@app.cell
def anchor_task_1():
    mo.Html('<div id="task_1"></div>')

@app.cell
def pell_status():

    # 1 reactive state for this variable
    get_choice, set_choice = mo.state(None)

    # 2 flag buttons
    include_btn = mo.ui.button(
        label="Include", kind="success", on_click=lambda _: set_choice("include")
    )
    exclude_btn = mo.ui.button(
        label="Exclude", kind="danger",  on_click=lambda _: set_choice("exclude")
    )
    flag_btn = mo.ui.button(
        label="Flag for Review", kind="warn", on_click=lambda _: set_choice("flag")
    )

    # 3 put buttons in an accordion 
    content = mo.vstack([
        mo.md(
            "Whether a student receives a federal Pell Grant. "
            "New regulations restrict use of financial-aid data in predictive modeling."
        ),
        mo.hstack([include_btn, exclude_btn, flag_btn], gap="1rem"),
    ])
    mo.accordion({"Pell Status": content})

    # 4 return the getter so other cells can react to it
    return get_choice

@app.cell
def pell_feedback(get_choice):

    # 1 read the current flag
    choice = get_choice()

    # 2 maps for emoji and label
    emoji_map = {
        "include": "🟢",
        "exclude": "🔴",
        "flag":    "🟡",
        None:      "⚪️",
    }
    text_map = {
        "include": "Include",
        "exclude": "Exclude",
        "flag":    "Flag for Review",
        None:      "no selection",
    }

    # 3 wrap in mo.md so this cell re-runs whenever choice changes
    mo.md(f"You decided to {emoji_map[choice]} **{text_map[choice]}** the variable.")


@app.cell
def pell_justification(get_choice):
    # 1 read current Pell selection
    pell_text_choice = get_choice()

    # 2 state holder for the justification text
    get_text_just_pell, set_text_just_pell = mo.state("")

    # 3 show textarea only after user picks Include / Exclude / Flag
    content_just_pell = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Pell Status choice",
            value=get_text_just_pell(),
            on_change=lambda v: set_text_just_pell(v),
            rows=4,
        )
        if pell_text_choice is not None
        else mo.md("")          
    )

    content_just_pell   

@app.cell
def efc_status():

    # 1 reactive state for this variable
    get_efc_choice, set_efc_choice = mo.state(None)

    # 2 flag buttons
    efc_include_btn = mo.ui.button(
        label="Include", kind="success", on_click=lambda _: set_efc_choice("include")
    )
    efc_exclude_btn = mo.ui.button(
        label="Exclude", kind="danger",  on_click=lambda _: set_efc_choice("exclude")
    )
    efc_flag_btn = mo.ui.button(
        label="Flag for Review", kind="warn", on_click=lambda _: set_efc_choice("flag")
    )

    # 3 put buttons in an accordion (or any layout you like)
    efc_content = mo.vstack([
        mo.md(
            "Amount a family is expected to contribute to education costs "
            "(legacy FAFSA metric). Regulatory compliance requires excluding "
            "this sensitive financial information."
        ),
        mo.hstack([efc_include_btn, efc_exclude_btn, efc_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Expected Family Contribution (EFC)": efc_content})

    # 4 return the getter so other cells can react to it
    return get_efc_choice

@app.cell
def efc_feedback(get_efc_choice):

    # 1 read the current flag
    efc_choice = get_efc_choice()

    # 2 maps for emoji and label
    efc_emoji_map = {
        "include": "🟢",
        "exclude": "🔴",
        "flag":    "🟡",
        None:      "⚪️",
    }
    efc_text_map = {
        "include": "Include",
        "exclude": "Exclude",
        "flag":    "Flag for Review",
        None:      "no selection",
    }

    # 3 wrap in mo.md so this cell re-runs whenever choice changes
    mo.md(f"You decided to {efc_emoji_map[efc_choice]} **{efc_text_map[efc_choice]}** the variable.")


@app.cell
def efc_justification(get_efc_choice):
    # 1 read current EFC selection
    efc_text_choice = get_efc_choice()

    # 2 state holder for the justification text
    get_text_just_efc, set_text_just_efc = mo.state("")

    # 3 show textarea only after user picks Include / Exclude / Flag
    content_just_efc = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your EFC choice",
            value=get_text_just_efc(),
            on_change=lambda v: set_text_just_efc(v),
            rows=4,
        )
        if efc_text_choice is not None
        else mo.md("")          
    )

    content_just_efc   

@app.cell
def sai_status():
    # 1) reactive state for SAI
    get_sai_choice, set_sai_choice = mo.state(None)

    # 2) flag buttons (all kwargs)
    sai_inc_btn  = mo.ui.button(
        label="Include",
        kind="success",
        on_click=lambda _: set_sai_choice("include"),
    )
    sai_exc_btn  = mo.ui.button(
        label="Exclude",
        kind="danger",
        on_click=lambda _: set_sai_choice("exclude"),
    )
    sai_flag_btn = mo.ui.button(
        label="Flag for Review",
        kind="warn",
        on_click=lambda _: set_sai_choice("flag"),
    )

    # 3) accordion content
    sai_content = mo.vstack([
        mo.md(
            "A new metric from recent FAFSA changes that replaced EFC. "
            "Recent implementation means this data may not be available for all "
            "students in your historical dataset."
        ),
        mo.hstack([sai_inc_btn, sai_exc_btn, sai_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Student Aid Index (SAI)": sai_content})

    # 4) expose getter
    return get_sai_choice

@app.cell
def sai_feedback(get_sai_choice):
    # current flag
    sai_choice = get_sai_choice()

    # emoji / text maps
    sai_emoji_map = {
        "include": "🟢",
        "exclude": "🔴",
        "flag":    "🟡",
        None:      "⚪️",
    }
    sai_text_map = {
        "include": "Include",
        "exclude": "Exclude",
        "flag":    "Flag for Review",
        None:      "no selection",
    }

    # show live feedback line
    mo.md(
        f"You decided to {sai_emoji_map[sai_choice]} "
        f"**{sai_text_map[sai_choice]}** the variable."
    )

@app.cell
def sai_justification(get_sai_choice):
    # read current SAI selection (unique local name)
    sai_selected_flag = get_sai_choice()

    # state holder for SAI justification text
    get_text_just_sai, set_text_just_sai = mo.state("")

    # show textarea only after a flag is chosen
    content_just_sai = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your SAI choice",
            value=get_text_just_sai(),
            on_change=lambda v: set_text_just_sai(v),
            rows=4,
        )
        if sai_selected_flag is not None
        else mo.md("")          # nothing yet
    )

    content_just_sai   # final expression rendered by the cell


# Unmet Need 
@app.cell
def unmet_status():
    # reactive state for Unmet Need
    get_unmet_choice, set_unmet_choice = mo.state(None)

    # buttons (all kwargs)
    unmet_inc_btn  = mo.ui.button(
        label="Include",
        kind="success",
        on_click=lambda _: set_unmet_choice("include"),
    )
    unmet_exc_btn  = mo.ui.button(
        label="Exclude",
        kind="danger",
        on_click=lambda _: set_unmet_choice("exclude"),
    )
    unmet_flag_btn = mo.ui.button(
        label="Flag for Review",
        kind="warn",
        on_click=lambda _: set_unmet_choice("flag"),
    )

    # accordion content
    unmet_content = mo.vstack([
        mo.md(
            "Gap between the cost of attendance and the student’s available resources. "
            "Financial-stress indicator, but regulatory restrictions likely prohibit "
            "its use in individual-level models."
        ),
        mo.hstack([unmet_inc_btn, unmet_exc_btn, unmet_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Unmet Need": unmet_content})

    # expose getter
    return get_unmet_choice

@app.cell
def unmet_feedback(get_unmet_choice):
    unmet_choice = get_unmet_choice()

    unmet_emoji_map = {
        "include": "🟢",
        "exclude": "🔴",
        "flag":    "🟡",
        None:      "⚪️",
    }
    unmet_text_map = {
        "include": "Include",
        "exclude": "Exclude",
        "flag":    "Flag for Review",
        None:      "no selection",
    }

    mo.md(
        f"You decided to {unmet_emoji_map[unmet_choice]} "
        f"**{unmet_text_map[unmet_choice]}** the variable."
    )

@app.cell
def unmet_justification(get_unmet_choice):
    unmet_selected_flag = get_unmet_choice()

    # text state
    get_text_just_unmet, set_text_just_unmet = mo.state("")

    content_just_unmet = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Unmet Need choice",
            value=get_text_just_unmet(),
            on_change=lambda v: set_text_just_unmet(v),
            rows=4,
        )
        if unmet_selected_flag is not None
        else mo.md("")
    )

    content_just_unmet   # rendered

@app.cell
def merit_status():
    # state for Merit Award Amount
    get_merit_choice, set_merit_choice = mo.state(None)

    # buttons
    merit_inc_btn  = mo.ui.button(
        label="Include",
        kind="success",
        on_click=lambda _: set_merit_choice("include"),
    )
    merit_exc_btn  = mo.ui.button(
        label="Exclude",
        kind="danger",
        on_click=lambda _: set_merit_choice("exclude"),
    )
    merit_flag_btn = mo.ui.button(
        label="Flag for Review",
        kind="warn",
        on_click=lambda _: set_merit_choice("flag"),
    )

    # accordion content
    merit_content = mo.vstack([
        mo.md(
            "Scholarship amounts awarded based on academic achievement rather than "
            "financial need. Consider whether this variable primarily reflects prior "
            "achievement or introduces socioeconomic factors into your model."
        ),
        mo.hstack([merit_inc_btn, merit_exc_btn, merit_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Merit Award Amount": merit_content})

    return get_merit_choice

@app.cell
def merit_feedback(get_merit_choice):
    merit_choice = get_merit_choice()

    merit_emoji_map = {
        "include": "🟢",
        "exclude": "🔴",
        "flag":    "🟡",
        None:      "⚪️",
    }
    merit_text_map = {
        "include": "Include",
        "exclude": "Exclude",
        "flag":    "Flag for Review",
        None:      "no selection",
    }

    mo.md(
        f"You decided to {merit_emoji_map[merit_choice]} "
        f"**{merit_text_map[merit_choice]}** the variable."
    )

@app.cell
def merit_justification(get_merit_choice):
    merit_selected_flag = get_merit_choice()

    get_text_just_merit, set_text_just_merit = mo.state("")

    content_just_merit = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Merit Award choice",
            value=get_text_just_merit(),
            on_change=lambda v: set_text_just_merit(v),
            rows=4,
        )
        if merit_selected_flag is not None
        else mo.md("")
    )

    content_just_merit  # rendered



@app.cell
def pplus_status():
    # state for Pell Plus
    get_pplus_choice, set_pplus_choice = mo.state(None)

    # buttons
    pplus_inc_btn  = mo.ui.button(
        label="Include",
        kind="success",
        on_click=lambda _: set_pplus_choice("include"),
    )
    pplus_exc_btn  = mo.ui.button(
        label="Exclude",
        kind="danger",
        on_click=lambda _: set_pplus_choice("exclude"),
    )
    pplus_flag_btn = mo.ui.button(
        label="Flag for Review",
        kind="warn",
        on_click=lambda _: set_pplus_choice("flag"),
    )

    # accordion content
    pplus_content = mo.vstack([
        mo.md(
            "University matching funds that complement federal Pell Grants. "
            "Financial-aid variables like this are likely subject to the same "
            "regulatory restrictions as other financial data."
        ),
        mo.hstack([pplus_inc_btn, pplus_exc_btn, pplus_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Pell Plus": pplus_content})

    return get_pplus_choice

@app.cell
def pplus_feedback(get_pplus_choice):
    pplus_choice = get_pplus_choice()

    pplus_emoji_map = {
        "include": "🟢",
        "exclude": "🔴",
        "flag":    "🟡",
        None:      "⚪️",
    }
    pplus_text_map = {
        "include": "Include",
        "exclude": "Exclude",
        "flag":    "Flag for Review",
        None:      "no selection",
    }

    mo.md(
        f"You decided to {pplus_emoji_map[pplus_choice]} "
        f"**{pplus_text_map[pplus_choice]}** the variable."
    )

@app.cell
def pplus_justification(get_pplus_choice):
    pplus_selected_flag = get_pplus_choice()

    get_text_just_pplus, set_text_just_pplus = mo.state("")

    content_just_pplus = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Pell Plus choice",
            value=get_text_just_pplus(),
            on_change=lambda v: set_text_just_pplus(v),
            rows=4,
        )
        if pplus_selected_flag is not None
        else mo.md("")
    )

    content_just_pplus


# Detailed Feedback on all variables
@app.cell
def detailed_feedback(
    get_choice,          # Pell
    get_efc_choice,      # EFC
    get_sai_choice,      # SAI
    get_unmet_choice,    # Unmet
    get_merit_choice,    # MErit
    get_pplus_choice,    # PPlus
):

    # read each variable’s choice
    choice_pell  = get_choice()
    choice_efc   = get_efc_choice()
    choice_sai   = get_sai_choice()
    choice_unmet = get_unmet_choice()
    choice_merit  = get_merit_choice()
    choice_pplus  = get_pplus_choice()

    # ----- Pell message
    if choice_pell == "exclude":
        msg_pell = "Right call"
    elif choice_pell == "flag":
        msg_pell = "Flagged"
    elif choice_pell == "include":
        msg_pell = (
            "Including Pell Status violates current federal guidance and may expose "
            "the institution to penalties. Consider aggregate reporting instead of "
            "individual-level use."
        )
    else:
        msg_pell = ""

    # ----- EFC message
    if choice_efc == "exclude":
        msg_efc = "Right call"
    elif choice_efc == "flag":
        msg_efc = "Flagged"
    elif choice_efc == "include":
        msg_efc = (
            "EFC is explicitly barred under 2024 Department of Education rules; "
            "its inclusion would render the model non-compliant."
        )
    else:
        msg_efc = ""

    # ----- SAI message
    if choice_sai == "exclude":
        msg_sai = "Right call"
    elif choice_sai == "flag":
        msg_sai = "Flagged"
    elif choice_sai == "include":
        msg_sai = (
            "SAI is sensitive financial-aid data with incomplete coverage. "
            "Using it risks privacy violations and injects missing-data bias."
        )
    else:
        msg_sai = ""

    # --- Unmet Need msg ---
    if choice_unmet == "exclude":
        msg_unmet = "Right call"
    elif choice_unmet == "flag":
        msg_unmet = "Flagged"
    elif choice_unmet == "include":
        msg_unmet = (
            "Unmet Need combines multiple restricted data points. Including it would "
            "contravene policy and amplify socioeconomic bias."
        )
    else:
        msg_unmet = ""
    
    # --- Merit Award msg ---
    if choice_merit == "exclude":
        msg_merit = "Right call"
    elif choice_merit == "flag":
        msg_merit = "Flagged"
    elif choice_merit == "include":
        msg_merit = (
            "Merit awards can proxy socioeconomic status and unintentionally "
            "disadvantage low-income students. Use only with a strong equity "
            "justification."
        )
    else:
        msg_merit = ""
        
    # --- Pell Plus msg ---
    if choice_pplus == "exclude":
        msg_pplus = "Right call"
    elif choice_pplus == "flag":
        msg_pplus = "Flagged"
    elif choice_pplus == "include":
        msg_pplus = (
            "Pell Plus directly signals Pell participation; individual-level use "
            "is restricted. Exclude or seek explicit legal clearance."
        )
    else:
        msg_pplus = ""


    # build accordion content
    content_detail_feedback = mo.vstack([
        mo.md(f"**Pell :** {msg_pell}"),
        mo.md(f"**EFC  :** {msg_efc}"),
        mo.md(f"**SAI  :** {msg_sai}"),
        mo.md(f"**Unmet :** {msg_unmet}"),
        mo.md(f"**Merit  :** {msg_merit}"),
        mo.md(f"**Pell+  :** {msg_pplus}"),
    ])

    mo.accordion({"Detailed Feedback": content_detail_feedback})


@app.cell
def section_separator():
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)

# ------------------------------------------------------------
# Task 2 – Protected-Attribute Gate
# ------------------------------------------------------------
@app.cell
def anchor_task_2():
    mo.Html('<div id="task_2"></div>')

@app.cell
def task_2():
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



@app.cell
def race_status():
    get_race_choice, set_race_choice = mo.state(None)

    race_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_race_choice("include_as_is")
    )
    race_audit_btn = mo.ui.button(
        label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_race_choice("audit_only")
    )
    race_exc_btn = mo.ui.button(
        label="Exclude Entirely", kind="danger", on_click=lambda _: set_race_choice("exclude_entirely")
    )

    race_content = mo.vstack([
        mo.md("Student’s self-reported racial/ethnic identity. Used during exploratory data analysis but removed before predictive modeling."),
        mo.hstack([race_inc_btn, race_audit_btn, race_exc_btn], gap="1rem"),
    ])
    mo.accordion({"Race": race_content})

    return get_race_choice

@app.cell
def race_feedback(get_race_choice):
    race_choice = get_race_choice()

    race_emoji_map = {
        "include_as_is": "🟢",
        "audit_only": "🟠",
        "exclude_entirely": "🔴",
        None: "⚪️",
    }
    race_text_map = {
        "include_as_is": "Include as-is",
        "audit_only": "Keep for Bias-Audit Only",
        "exclude_entirely": "Exclude Entirely",
        None: "no selection",
    }

    mo.md(f"You decided to {race_emoji_map[race_choice]} **{race_text_map[race_choice]}** the variable.")

@app.cell
def race_justification(get_race_choice):
    race_selected_flag = get_race_choice()
    get_text_just_race, set_text_just_race = mo.state("")

    content_just_race = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Race choice",
            value=get_text_just_race(),
            on_change=lambda v: set_text_just_race(v),
            rows=4,
        )
        if race_selected_flag is not None
        else mo.md("")
    )
    content_just_race

@app.cell
def gender_status():
    get_gender_choice, set_gender_choice = mo.state(None)

    gender_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_gender_choice("include_as_is")
    )
    gender_audit_btn = mo.ui.button(
        label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_gender_choice("audit_only")
    )
    gender_exc_btn = mo.ui.button(
        label="Exclude Entirely", kind="danger", on_click=lambda _: set_gender_choice("exclude_entirely")
    )

    gender_content = mo.vstack([
        mo.md("Student’s gender identity as reported during application. Protected class variable that raises ethical considerations."),
        mo.hstack([gender_inc_btn, gender_audit_btn, gender_exc_btn], gap="1rem"),
    ])
    mo.accordion({"Gender": gender_content})

    return get_gender_choice

@app.cell
def gender_feedback(get_gender_choice):
    gender_choice = get_gender_choice()

    gender_emoji_map = {
        "include_as_is": "🟢",
        "audit_only": "🟠",
        "exclude_entirely": "🔴",
        None: "⚪️",
    }
    gender_text_map = {
        "include_as_is": "Include as-is",
        "audit_only": "Keep for Bias-Audit Only",
        "exclude_entirely": "Exclude Entirely",
        None: "no selection",
    }

    mo.md(f"You decided to {gender_emoji_map[gender_choice]} **{gender_text_map[gender_choice]}** the variable.")

@app.cell
def gender_justification(get_gender_choice):
    gender_selected_flag = get_gender_choice()
    get_text_just_gender, set_text_just_gender = mo.state("")

    content_just_gender = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Gender choice",
            value=get_text_just_gender(),
            on_change=lambda v: set_text_just_gender(v),
            rows=4,
        )
        if gender_selected_flag is not None
        else mo.md("")
    )
    content_just_gender

@app.cell
def age_status():
    get_age_choice, set_age_choice = mo.state(None)

    age_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_age_choice("include_as_is")
    )
    age_audit_btn = mo.ui.button(
        label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_age_choice("audit_only")
    )
    age_exc_btn = mo.ui.button(
        label="Exclude Entirely", kind="danger", on_click=lambda _: set_age_choice("exclude_entirely")
    )

    age_content = mo.vstack([
        mo.md("Student’s age at enrollment. Flagged as protected class variable. Consider whether age-based predictions might disadvantage non-traditional students while recognizing that age can reflect meaningful differences in life circumstances."),
        mo.hstack([age_inc_btn, age_audit_btn, age_exc_btn], gap="1rem"),
    ])
    mo.accordion({"Age": age_content})

    return get_age_choice

@app.cell
def age_feedback(get_age_choice):
    age_choice = get_age_choice()

    age_emoji_map = {
        "include_as_is": "🟢",
        "audit_only": "🟠",
        "exclude_entirely": "🔴",
        None: "⚪️",
    }
    age_text_map = {
        "include_as_is": "Include as-is",
        "audit_only": "Keep for Bias-Audit Only",
        "exclude_entirely": "Exclude Entirely",
        None: "no selection",
    }

    mo.md(f"You decided to {age_emoji_map[age_choice]} **{age_text_map[age_choice]}** the variable.")

@app.cell
def age_justification(get_age_choice):
    age_selected_flag = get_age_choice()
    get_text_just_age, set_text_just_age = mo.state("")

    content_just_age = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Age choice",
            value=get_text_just_age(),
            on_change=lambda v: set_text_just_age(v),
            rows=4,
        )
        if age_selected_flag is not None
        else mo.md("")
    )
    content_just_age


@app.cell
def pronouns_status():
    get_pronouns_choice, set_pronouns_choice = mo.state(None)

    pronouns_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_pronouns_choice("include_as_is")
    )
    pronouns_audit_btn = mo.ui.button(
        label="Keep for Bias-Audit Only", kind="warn", on_click=lambda _: set_pronouns_choice("audit_only")
    )
    pronouns_exc_btn = mo.ui.button(
        label="Exclude Entirely", kind="danger", on_click=lambda _: set_pronouns_choice("exclude_entirely")
    )

    pronouns_content = mo.vstack([
        mo.md("Student-provided pronoun preference collected by campus climate office. Optional field with high missingness. Can affirm identity but is not a stable predictor of retention."),
        mo.hstack([pronouns_inc_btn, pronouns_audit_btn, pronouns_exc_btn], gap="1rem"),
    ])
    mo.accordion({"Preferred Pronouns": pronouns_content})

    return get_pronouns_choice

@app.cell
def pronouns_feedback(get_pronouns_choice):
    pronouns_choice = get_pronouns_choice()

    pronouns_emoji_map = {
        "include_as_is": "🟢",
        "audit_only": "🟠",
        "exclude_entirely": "🔴",
        None: "⚪️",
    }
    pronouns_text_map = {
        "include_as_is": "Include as-is",
        "audit_only": "Keep for Bias-Audit Only",
        "exclude_entirely": "Exclude Entirely",
        None: "no selection",
    }

    mo.md(f"You decided to {pronouns_emoji_map[pronouns_choice]} **{pronouns_text_map[pronouns_choice]}** the variable.")

@app.cell
def pronouns_justification(get_pronouns_choice):
    pronouns_selected_flag = get_pronouns_choice()
    get_text_just_pronouns, set_text_just_pronouns = mo.state("")

    content_just_pronouns = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Preferred Pronouns choice",
            value=get_text_just_pronouns(),
            on_change=lambda v: set_text_just_pronouns(v),
            rows=4,
        )
        if pronouns_selected_flag is not None
        else mo.md("")
    )
    content_just_pronouns

@app.cell
def detailed_feedback_task2(
    get_race_choice,
    get_gender_choice,
    get_age_choice,
    get_pronouns_choice
):
    # ----- Race message
    race = get_race_choice()
    if race == "include_as_is":
        msg_race = "Using Race as a predictive feature can embed historical inequities and violate institutional policy. Retain only for bias-audit."
    elif race == "audit_only":
        msg_race = "Right call"
    elif race == "exclude_entirely":
        msg_race = "Without Race you lose the ability to audit fair outcomes across groups. Best practice is to keep it for auditing while excluding it from model training."
    else:
        msg_race = ""

    # ----- Gender message
    gender = get_gender_choice()
    if gender == "include_as_is":
        msg_gender = "Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention."
    elif gender == "audit_only":
        msg_gender = "Right call"
    elif gender == "exclude_entirely":
        msg_gender = "Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs."
    else:
        msg_gender = ""

    # ----- Age message
    age = get_age_choice()
    if age == "include_as_is":
        msg_age = "Age may correlate with persistence but also with protected status (non-traditional learners). Document equity safeguards or shift to audit-only use."
    elif age == "audit_only":
        msg_age = "Right call"
    elif age == "exclude_entirely":
        msg_age = "Excluding Age erases patterns relevant to adult learners and hampers fairness checks. Audit-only use is often a balanced choice."
    else:
        msg_age = ""

    # ----- Pronouns message
    pronouns = get_pronouns_choice()
    if pronouns == "include_as_is":
        msg_pronouns = "Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. Exclude or store only for awareness training, not analytics."
    elif pronouns == "audit_only":
        msg_pronouns = "Pronoun data lack completeness and standardization, limiting audit utility. Exclusion is usually appropriate."
    elif pronouns == "exclude_entirely":
        msg_pronouns = "Right call"
    else:
        msg_pronouns = ""

    content_detail_feedback2 = mo.vstack([
        mo.md(f"**Race:** {msg_race}"),
        mo.md(f"**Gender:** {msg_gender}"),
        mo.md(f"**Age:** {msg_age}"),
        mo.md(f"**Preferred Pronouns:** {msg_pronouns}"),
    ])

    mo.accordion({"Detailed Feedback – Task 2": content_detail_feedback2})

@app.cell
def section_separator():
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)

# ------------------------------------------------------------
# Task 3 – Data-Reliability Gate
# ------------------------------------------------------------
@app.cell
def anchor_task_3():
    mo.Html('<div id="task_3"></div>')

@app.cell
def task_3():
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



@app.cell
def hsgpa_status():
    get_hsgpa_choice, set_hsgpa_choice = mo.state(None)

    hsgpa_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_hsgpa_choice("include_as_is")
    )
    hsgpa_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_hsgpa_choice("exclude_unreliable")
    )
    hsgpa_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_hsgpa_choice("flag_improvement")
    )

    hsgpa_content = mo.vstack([
        mo.md(
            "Student’s high-school grade-point average, a common predictor of college success. "
            "This variable was unreliable due to reporting unreliability across high schools."
        ),
        mo.hstack([hsgpa_inc_btn, hsgpa_exc_btn, hsgpa_flag_btn], gap="1rem"),
    ])
    mo.accordion({"High-School GPA": hsgpa_content})

    return get_hsgpa_choice

@app.cell
def hsgpa_feedback(get_hsgpa_choice):
    hsgpa_choice = get_hsgpa_choice()

    hsgpa_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    hsgpa_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {hsgpa_emoji_map[hsgpa_choice]} **{hsgpa_text_map[hsgpa_choice]}** the variable.")

@app.cell
def hsgpa_justification(get_hsgpa_choice):
    hsgpa_selected_flag = get_hsgpa_choice()
    get_text_just_hsgpa, set_text_just_hsgpa = mo.state("")

    content_just_hsgpa = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your High-School GPA choice",
            value=get_text_just_hsgpa(),
            on_change=lambda v: set_text_just_hsgpa(v),
            rows=4,
        )
        if hsgpa_selected_flag is not None
        else mo.md("")
    )
    content_just_hsgpa


@app.cell
def tests_status():
    get_tests_choice, set_tests_choice = mo.state(None)

    tests_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_tests_choice("include_as_is")
    )
    tests_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_tests_choice("exclude_unreliable")
    )
    tests_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_tests_choice("flag_improvement")
    )

    tests_content = mo.vstack([
        mo.md(
            "Academic performance metrics from high school and standardised tests (SAT/ACT). "
            "Due to test-optional policies implemented during COVID, scores may be missing for many students. "
            "Creative solution to transform into a ‘test score submitted’ indicator leverages available information while addressing systematic gaps."
        ),
        mo.hstack([tests_inc_btn, tests_exc_btn, tests_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Test Scores": tests_content})

    return get_tests_choice

@app.cell
def tests_feedback(get_tests_choice):
    tests_choice = get_tests_choice()

    tests_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    tests_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {tests_emoji_map[tests_choice]} **{tests_text_map[tests_choice]}** the variable.")

@app.cell
def tests_justification(get_tests_choice):
    tests_selected_flag = get_tests_choice()
    get_text_just_tests, set_text_just_tests = mo.state("")

    content_just_tests = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Test Scores choice",
            value=get_text_just_tests(),
            on_change=lambda v: set_text_just_tests(v),
            rows=4,
        )
        if tests_selected_flag is not None
        else mo.md("")
    )
    content_just_tests


@app.cell
def midterm_status():
    get_midterm_choice, set_midterm_choice = mo.state(None)

    midterm_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_midterm_choice("include_as_is")
    )
    midterm_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_midterm_choice("exclude_unreliable")
    )
    midterm_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_midterm_choice("flag_improvement")
    )

    midterm_content = mo.vstack([
        mo.md(
            "Preliminary academic performance indicators halfway through the term. "
            "Identified as valuable but not consistently available across courses."
        ),
        mo.hstack([midterm_inc_btn, midterm_exc_btn, midterm_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Mid-Term Grades": midterm_content})

    return get_midterm_choice

@app.cell
def midterm_feedback(get_midterm_choice):
    midterm_choice = get_midterm_choice()

    midterm_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    midterm_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {midterm_emoji_map[midterm_choice]} **{midterm_text_map[midterm_choice]}** the variable.")

@app.cell
def midterm_justification(get_midterm_choice):
    midterm_selected_flag = get_midterm_choice()
    get_text_just_midterm, set_text_just_midterm = mo.state("")

    content_just_midterm = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Mid-Term Grades choice",
            value=get_text_just_midterm(),
            on_change=lambda v: set_text_just_midterm(v),
            rows=4,
        )
        if midterm_selected_flag is not None
        else mo.md("")
    )
    content_just_midterm


@app.cell
def epr_status():
    get_epr_choice, set_epr_choice = mo.state(None)

    epr_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_epr_choice("include_as_is")
    )
    epr_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_epr_choice("exclude_unreliable")
    )
    epr_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_epr_choice("flag_improvement")
    )

    epr_content = mo.vstack([
        mo.md(
            "Faculty-submitted assessments of student performance early in the semester. "
            "Reporting inconsistency means this potentially valuable early-warning indicator isn’t reliable enough to include."
        ),
        mo.hstack([epr_inc_btn, epr_exc_btn, epr_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Early Progress Reports": epr_content})

    return get_epr_choice

@app.cell
def epr_feedback(get_epr_choice):
    epr_choice = get_epr_choice()

    epr_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    epr_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {epr_emoji_map[epr_choice]} **{epr_text_map[epr_choice]}** the variable.")

@app.cell
def epr_justification(get_epr_choice):
    epr_selected_flag = get_epr_choice()
    get_text_just_epr, set_text_just_epr = mo.state("")

    content_just_epr = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Early Progress Reports choice",
            value=get_text_just_epr(),
            on_change=lambda v: set_text_just_epr(v),
            rows=4,
        )
        if epr_selected_flag is not None
        else mo.md("")
    )
    content_just_epr


@app.cell
def printer_status():
    get_printer_choice, set_printer_choice = mo.state(None)

    printer_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_printer_choice("include_as_is")
    )
    printer_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_printer_choice("exclude_unreliable")
    )
    printer_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_printer_choice("flag_improvement")
    )

    printer_content = mo.vstack([
        mo.md(
            "Weekly count of pages printed in residence-hall printers. "
            "Logs are missing whenever printers are offline; many students use personal or library printers instead."
        ),
        mo.hstack([printer_inc_btn, printer_exc_btn, printer_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Dorm-Printer Usage": printer_content})

    return get_printer_choice

@app.cell
def printer_feedback(get_printer_choice):
    printer_choice = get_printer_choice()

    printer_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    printer_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {printer_emoji_map[printer_choice]} **{printer_text_map[printer_choice]}** the variable.")

@app.cell
def printer_justification(get_printer_choice):
    printer_selected_flag = get_printer_choice()
    get_text_just_printer, set_text_just_printer = mo.state("")

    content_just_printer = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Dorm-Printer Usage choice",
            value=get_text_just_printer(),
            on_change=lambda v: set_text_just_printer(v),
            rows=4,
        )
        if printer_selected_flag is not None
        else mo.md("")
    )
    content_just_printer


@app.cell
def detailed_feedback_task3(
    get_hsgpa_choice,
    get_tests_choice,
    get_midterm_choice,
    get_epr_choice,
    get_printer_choice
):
    # --- High-School GPA ---
    hsgpa = get_hsgpa_choice()
    if hsgpa == "include_as_is":
        msg_hsgpa = "High-school GPAs lack standardisation; predictive value may be swamped by noise. Consider excluding or flagging for quality remediation."
    elif hsgpa == "exclude_unreliable":
        msg_hsgpa = "Removing High-School GPA sacrifices a widely used predictor. Could a scaled or percentile version salvage reliability?"
    elif hsgpa == "flag_improvement":
        msg_hsgpa = "Right call"
    else:
        msg_hsgpa = ""

    # --- Test Scores ---
    tests = get_tests_choice()
    if tests == "include_as_is":
        msg_tests = "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. A submission indicator or audit flag may be safer."
    elif tests == "exclude_unreliable":
        msg_tests = "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. Could you retain a binary ‘submitted’ flag instead?"
    elif tests == "flag_improvement":
        msg_tests = "Right call"
    else:
        msg_tests = ""

    # --- Mid-Term Grades ---
    midterm = get_midterm_choice()
    if midterm == "include_as_is":
        msg_midterm = "Mid-Term Grades appear only for certain courses, risking departmental bias. Flag for quality improvement or exclude."
    elif midterm == "exclude_unreliable":
        msg_midterm = "Excluding Mid-Term Grades forfeits early academic-performance insight. Could selective inclusion or data-quality work make it viable?"
    elif midterm == "flag_improvement":
        msg_midterm = "Right call"
    else:
        msg_midterm = ""

    # --- Early Progress Reports ---
    epr = get_epr_choice()
    if epr == "include_as_is":
        msg_epr = "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion."
    elif epr == "exclude_unreliable":
        msg_epr = "You lose a proven early-alert signal. Engage stakeholders to improve reporting rather than discard entirely."
    elif epr == "flag_improvement":
        msg_epr = "Right call"
    else:
        msg_epr = ""

    # --- Dorm-Printer Usage ---
    printer = get_printer_choice()
    if printer == "include_as_is":
        msg_printer = "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. Little theoretical link to persistence."
    elif printer == "flag_improvement":
        msg_printer = "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost."
    elif printer == "exclude_unreliable":
        msg_printer = "Appropriate—the variable is weakly linked to retention and suffers systemic gaps."
    else:
        msg_printer = ""

    content_detail_feedback3 = mo.vstack([
        mo.md(f"**High-School GPA:** {msg_hsgpa}"),
        mo.md(f"**Test Scores:** {msg_tests}"),
        mo.md(f"**Mid-Term Grades:** {msg_midterm}"),
        mo.md(f"**Early Progress Reports:** {msg_epr}"),
        mo.md(f"**Dorm-Printer Usage:** {msg_printer}"),
    ])

    mo.accordion({"Detailed Feedback – Task 3": content_detail_feedback3})

@app.cell
def section_separator():
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)

# ------------------------------------------------------------
# Task 4 – Equity & Actionability Gate
# ------------------------------------------------------------
@app.cell
def anchor_task_4():
    mo.Html('<div id="task_4"></div>')

@app.cell
def task_4():
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

# ------------------------------------------------------------
# Legacy Status
# ------------------------------------------------------------
@app.cell
def legacy_status():
    get_legacy_choice, set_legacy_choice = mo.state(None)

    legacy_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_legacy_choice("include_as_is")
    )
    legacy_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_legacy_choice("exclude_unreliable")
    )
    legacy_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_legacy_choice("flag_improvement")
    )

    legacy_content = mo.vstack([
        mo.md(
            "Whether the student has family members who previously attended the university. "
            "May indicate stronger institutional ties."
        ),
        mo.hstack([legacy_inc_btn, legacy_exc_btn, legacy_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Legacy Status": legacy_content})

    return get_legacy_choice

@app.cell
def legacy_feedback(get_legacy_choice):
    legacy_choice = get_legacy_choice()

    legacy_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    legacy_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {legacy_emoji_map[legacy_choice]} **{legacy_text_map[legacy_choice]}** the variable.")

@app.cell
def legacy_justification(get_legacy_choice):
    legacy_selected_flag = get_legacy_choice()
    get_text_just_legacy, set_text_just_legacy = mo.state("")

    content_just_legacy = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Legacy Status choice",
            value=get_text_just_legacy(),
            on_change=lambda v: set_text_just_legacy(v),
            rows=4,
        )
        if legacy_selected_flag is not None
        else mo.md("")
    )
    content_just_legacy

# ------------------------------------------------------------
# Student Athlete Status
# ------------------------------------------------------------
@app.cell
def athlete_status():
    get_athlete_choice, set_athlete_choice = mo.state(None)

    athlete_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_athlete_choice("include_as_is")
    )
    athlete_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_athlete_choice("exclude_unreliable")
    )
    athlete_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_athlete_choice("flag_improvement")
    )

    athlete_content = mo.vstack([
        mo.md(
            "Whether the student participates in university athletics. May indicate additional support structures but also time commitments."
        ),
        mo.hstack([athlete_inc_btn, athlete_exc_btn, athlete_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Student Athlete Status": athlete_content})

    return get_athlete_choice

@app.cell
def athlete_feedback(get_athlete_choice):
    athlete_choice = get_athlete_choice()

    athlete_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    athlete_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {athlete_emoji_map[athlete_choice]} **{athlete_text_map[athlete_choice]}** the variable.")

@app.cell
def athlete_justification(get_athlete_choice):
    athlete_selected_flag = get_athlete_choice()
    get_text_just_athlete, set_text_just_athlete = mo.state("")

    content_just_athlete = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Student Athlete Status choice",
            value=get_text_just_athlete(),
            on_change=lambda v: set_text_just_athlete(v),
            rows=4,
        )
        if athlete_selected_flag is not None
        else mo.md("")
    )
    content_just_athlete

# ------------------------------------------------------------
# First-Generation Student
# ------------------------------------------------------------
@app.cell
def firstgen_status():
    get_firstgen_choice, set_firstgen_choice = mo.state(None)

    firstgen_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_firstgen_choice("include_as_is")
    )
    firstgen_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_firstgen_choice("exclude_unreliable")
    )
    firstgen_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_firstgen_choice("flag_improvement")
    )

    firstgen_content = mo.vstack([
        mo.md(
            "Indicates if the student is the first in their family to attend college; may reflect differences in familiarity with college processes."
        ),
        mo.hstack([firstgen_inc_btn, firstgen_exc_btn, firstgen_flag_btn], gap="1rem"),
    ])
    mo.accordion({"First-Generation Student": firstgen_content})

    return get_firstgen_choice

@app.cell
def firstgen_feedback(get_firstgen_choice):
    firstgen_choice = get_firstgen_choice()

    firstgen_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    firstgen_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {firstgen_emoji_map[firstgen_choice]} **{firstgen_text_map[firstgen_choice]}** the variable.")

@app.cell
def firstgen_justification(get_firstgen_choice):
    firstgen_selected_flag = get_firstgen_choice()
    get_text_just_firstgen, set_text_just_firstgen = mo.state("")

    content_just_firstgen = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your First-Generation Student choice",
            value=get_text_just_firstgen(),
            on_change=lambda v: set_text_just_firstgen(v),
            rows=4,
        )
        if firstgen_selected_flag is not None
        else mo.md("")
    )
    content_just_firstgen


# ------------------------------------------------------------
# Distance from Home
# ------------------------------------------------------------
@app.cell
def distance_status():
    get_distance_choice, set_distance_choice = mo.state(None)

    distance_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_distance_choice("include_as_is")
    )
    distance_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_distance_choice("exclude_unreliable")
    )
    distance_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_distance_choice("flag_improvement")
    )

    distance_content = mo.vstack([
        mo.md(
            "Calculated metric based on student’s home address and campus location; privacy-preserving alternative to ZIP codes."
        ),
        mo.hstack([distance_inc_btn, distance_exc_btn, distance_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Distance from Home": distance_content})

    return get_distance_choice

@app.cell
def distance_feedback(get_distance_choice):
    distance_choice = get_distance_choice()

    distance_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    distance_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {distance_emoji_map[distance_choice]} **{distance_text_map[distance_choice]}** the variable.")

@app.cell
def distance_justification(get_distance_choice):
    distance_selected_flag = get_distance_choice()
    get_text_just_distance, set_text_just_distance = mo.state("")

    content_just_distance = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Distance from Home choice",
            value=get_text_just_distance(),
            on_change=lambda v: set_text_just_distance(v),
            rows=4,
        )
        if distance_selected_flag is not None
        else mo.md("")
    )
    content_just_distance

# ------------------------------------------------------------
# Credits After Add/Drop
# ------------------------------------------------------------
@app.cell
def credits_status():
    get_credits_choice, set_credits_choice = mo.state(None)

    credits_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_credits_choice("include_as_is")
    )
    credits_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_credits_choice("exclude_unreliable")
    )
    credits_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_credits_choice("flag_improvement")
    )

    credits_content = mo.vstack([
        mo.md(
            "Credit hours the student is taking after the official add/drop deadline; may reflect adjustment to academic realities."
        ),
        mo.hstack([credits_inc_btn, credits_exc_btn, credits_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Credits After Add/Drop": credits_content})

    return get_credits_choice

@app.cell
def credits_feedback(get_credits_choice):
    credits_choice = get_credits_choice()

    credits_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    credits_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {credits_emoji_map[credits_choice]} **{credits_text_map[credits_choice]}** the variable.")

@app.cell
def credits_justification(get_credits_choice):
    credits_selected_flag = get_credits_choice()
    get_text_just_credits, set_text_just_credits = mo.state("")

    content_just_credits = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Credits After Add/Drop choice",
            value=get_text_just_credits(),
            on_change=lambda v: set_text_just_credits(v),
            rows=4,
        )
        if credits_selected_flag is not None
        else mo.md("")
    )
    content_just_credits

# ------------------------------------------------------------
# Live On-Campus or Commuter
# ------------------------------------------------------------
@app.cell
def livecampus_status():
    get_livecampus_choice, set_livecampus_choice = mo.state(None)

    livecampus_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_livecampus_choice("include_as_is")
    )
    livecampus_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_livecampus_choice("exclude_unreliable")
    )
    livecampus_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_livecampus_choice("flag_improvement")
    )

    livecampus_content = mo.vstack([
        mo.md(
            "Housing status affects integration into campus life and access to resources."
        ),
        mo.hstack([livecampus_inc_btn, livecampus_exc_btn, livecampus_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Live On-Campus or Commuter": livecampus_content})

    return get_livecampus_choice

@app.cell
def livecampus_feedback(get_livecampus_choice):
    livecampus_choice = get_livecampus_choice()

    livecampus_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    livecampus_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {livecampus_emoji_map[livecampus_choice]} **{livecampus_text_map[livecampus_choice]}** the variable.")

@app.cell
def livecampus_justification(get_livecampus_choice):
    livecampus_selected_flag = get_livecampus_choice()
    get_text_just_livecampus, set_text_just_livecampus = mo.state("")

    content_just_livecampus = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Live On-Campus or Commuter choice",
            value=get_text_just_livecampus(),
            on_change=lambda v: set_text_just_livecampus(v),
            rows=4,
        )
        if livecampus_selected_flag is not None
        else mo.md("")
    )
    content_just_livecampus

# ------------------------------------------------------------
# Residency (In-State / Out-of-State / International)
# ------------------------------------------------------------
@app.cell
def residency_status():
    get_residency_choice, set_residency_choice = mo.state(None)

    residency_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_residency_choice("include_as_is")
    )
    residency_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_residency_choice("exclude_unreliable")
    )
    residency_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_residency_choice("flag_improvement")
    )

    residency_content = mo.vstack([
        mo.md(
            "Affects tuition rates and connection to campus."
        ),
        mo.hstack([residency_inc_btn, residency_exc_btn, residency_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Residency (In-State / Out-of-State / International)": residency_content})

    return get_residency_choice

@app.cell
def residency_feedback(get_residency_choice):
    residency_choice = get_residency_choice()

    residency_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    residency_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {residency_emoji_map[residency_choice]} **{residency_text_map[residency_choice]}** the variable.")

@app.cell
def residency_justification(get_residency_choice):
    residency_selected_flag = get_residency_choice()
    get_text_just_residency, set_text_just_residency = mo.state("")

    content_just_residency = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Residency choice",
            value=get_text_just_residency(),
            on_change=lambda v: set_text_just_residency(v),
            rows=4,
        )
        if residency_selected_flag is not None
        else mo.md("")
    )
    content_just_residency

# ------------------------------------------------------------
# Urban / Rural / Suburban Origin
# ------------------------------------------------------------
@app.cell
def origin_status():
    get_origin_choice, set_origin_choice = mo.state(None)

    origin_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_origin_choice("include_as_is")
    )
    origin_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_origin_choice("exclude_unreliable")
    )
    origin_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_origin_choice("flag_improvement")
    )

    origin_content = mo.vstack([
        mo.md(
            "Classification of student’s home community; derived from heuristics."
        ),
        mo.hstack([origin_inc_btn, origin_exc_btn, origin_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Urban / Rural / Suburban Origin": origin_content})

    return get_origin_choice

@app.cell
def origin_feedback(get_origin_choice):
    origin_choice = get_origin_choice()

    origin_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    origin_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {origin_emoji_map[origin_choice]} **{origin_text_map[origin_choice]}** the variable.")

@app.cell
def origin_justification(get_origin_choice):
    origin_selected_flag = get_origin_choice()
    get_text_just_origin, set_text_just_origin = mo.state("")

    content_just_origin = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Urban / Rural / Suburban Origin choice",
            value=get_text_just_origin(),
            on_change=lambda v: set_text_just_origin(v),
            rows=4,
        )
        if origin_selected_flag is not None
        else mo.md("")
    )
    content_just_origin

# ------------------------------------------------------------
# Transfer Status
# ------------------------------------------------------------
@app.cell
def transfer_status():
    get_transfer_choice, set_transfer_choice = mo.state(None)

    transfer_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_transfer_choice("include_as_is")
    )
    transfer_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_transfer_choice("exclude_unreliable")
    )
    transfer_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_transfer_choice("flag_improvement")
    )

    transfer_content = mo.vstack([
        mo.md(
            "Whether the student transferred from another institution versus starting as a first-year."
        ),
        mo.hstack([transfer_inc_btn, transfer_exc_btn, transfer_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Transfer Status": transfer_content})

    return get_transfer_choice

@app.cell
def transfer_feedback(get_transfer_choice):
    transfer_choice = get_transfer_choice()

    transfer_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    transfer_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {transfer_emoji_map[transfer_choice]} **{transfer_text_map[transfer_choice]}** the variable.")

@app.cell
def transfer_justification(get_transfer_choice):
    transfer_selected_flag = get_transfer_choice()
    get_text_just_transfer, set_text_just_transfer = mo.state("")

    content_just_transfer = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Transfer Status choice",
            value=get_text_just_transfer(),
            on_change=lambda v: set_text_just_transfer(v),
            rows=4,
        )
        if transfer_selected_flag is not None
        else mo.md("")
    )
    content_just_transfer

# ------------------------------------------------------------
# Extracurricular Involvement
# ------------------------------------------------------------
@app.cell
def extracurricular_status():
    get_extracurricular_choice, set_extracurricular_choice = mo.state(None)

    extracurricular_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_extracurricular_choice("include_as_is")
    )
    extracurricular_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_extracurricular_choice("exclude_unreliable")
    )
    extracurricular_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_extracurricular_choice("flag_improvement")
    )

    extracurricular_content = mo.vstack([
        mo.md(
            "Participation in clubs or other non-academic activities; data collection relies on self-reporting."
        ),
        mo.hstack([extracurricular_inc_btn, extracurricular_exc_btn, extracurricular_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Extracurricular Involvement": extracurricular_content})

    return get_extracurricular_choice

@app.cell
def extracurricular_feedback(get_extracurricular_choice):
    extracurricular_choice = get_extracurricular_choice()

    extracurricular_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    extracurricular_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {extracurricular_emoji_map[extracurricular_choice]} **{extracurricular_text_map[extracurricular_choice]}** the variable.")

@app.cell
def extracurricular_justification(get_extracurricular_choice):
    extracurricular_selected_flag = get_extracurricular_choice()
    get_text_just_extracurricular, set_text_just_extracurricular = mo.state("")

    content_just_extracurricular = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Extracurricular Involvement choice",
            value=get_text_just_extracurricular(),
            on_change=lambda v: set_text_just_extracurricular(v),
            rows=4,
        )
        if extracurricular_selected_flag is not None
        else mo.md("")
    )
    content_just_extracurricular

# ------------------------------------------------------------
# Campus-Wi-Fi Gaming Network Participation (Distractor)
# ------------------------------------------------------------
@app.cell
def gaming_status():
    get_gaming_choice, set_gaming_choice = mo.state(None)

    gaming_inc_btn = mo.ui.button(
        label="Include as-is", kind="success", on_click=lambda _: set_gaming_choice("include_as_is")
    )
    gaming_exc_btn = mo.ui.button(
        label="Exclude (too unreliable)", kind="danger", on_click=lambda _: set_gaming_choice("exclude_unreliable")
    )
    gaming_flag_btn = mo.ui.button(
        label="Flag for Data-Quality Improvement", kind="warn", on_click=lambda _: set_gaming_choice("flag_improvement")
    )

    gaming_content = mo.vstack([
        mo.md(
            "Binary flag—student devices connected to high-traffic gaming ports for ≥ 5 hours/week during evenings."
        ),
        mo.hstack([gaming_inc_btn, gaming_exc_btn, gaming_flag_btn], gap="1rem"),
    ])
    mo.accordion({"Campus-Wi-Fi Gaming Network Participation": gaming_content})

    return get_gaming_choice

@app.cell
def gaming_feedback(get_gaming_choice):
    gaming_choice = get_gaming_choice()

    gaming_emoji_map = {
        "include_as_is": "🟢",
        "exclude_unreliable": "🔴",
        "flag_improvement": "🟠",
        None: "⚪️",
    }
    gaming_text_map = {
        "include_as_is": "Include as-is",
        "exclude_unreliable": "Exclude (too unreliable)",
        "flag_improvement": "Flag for Data-Quality Improvement",
        None: "no selection",
    }

    mo.md(f"You decided to {gaming_emoji_map[gaming_choice]} **{gaming_text_map[gaming_choice]}** the variable.")

@app.cell
def gaming_justification(get_gaming_choice):
    gaming_selected_flag = get_gaming_choice()
    get_text_just_gaming, set_text_just_gaming = mo.state("")

    content_just_gaming = (
        mo.ui.text_area(
            label="Please briefly justify your reasoning for your Campus-Wi-Fi Gaming choice",
            value=get_text_just_gaming(),
            on_change=lambda v: set_text_just_gaming(v),
            rows=4,
        )
        if gaming_selected_flag is not None
        else mo.md("")
    )
    content_just_gaming

# ------------------------------------------------------------
# Detailed Feedback – Task 4
# ------------------------------------------------------------
@app.cell
def detailed_feedback_task4(
    get_legacy_choice,
    get_athlete_choice,
    get_firstgen_choice,
    get_distance_choice,
    get_credits_choice,
    get_livecampus_choice,
    get_residency_choice,
    get_origin_choice,
    get_transfer_choice,
    get_extracurricular_choice,
    get_gaming_choice
):
    # --- Legacy Status ---
    legacy = get_legacy_choice()
    if legacy == "include_as_is":
        msg_legacy = "Legacy Status may encode privilege and could unfairly prioritise well-connected students. Document why its predictive gain outweighs equity concerns."
    elif legacy == "exclude_unreliable":
        msg_legacy = "You removed a factor linked to institutional attachment. Could advisors design fair interventions if they knew a student lacked legacy ties?"
    elif legacy == "flag_improvement":
        msg_legacy = "Right call"
    else:
        msg_legacy = ""

    # --- Student Athlete Status ---
    athlete = get_athlete_choice()
    if athlete == "include_as_is":
        msg_athlete = "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. Ensure interventions add value."
    elif athlete == "exclude_unreliable":
        msg_athlete = "Athletes juggle academics and sport travel. Excluding this variable may hide a known risk group lacking time for coursework."
    elif athlete == "flag_improvement":
        msg_athlete = "Right call"
    else:
        msg_athlete = ""

    # --- First-Generation Student ---
    firstgen = get_firstgen_choice()
    if firstgen == "include_as_is":
        msg_firstgen = "Good call—first-gen status supports equity-minded outreach. Be sure to explain positive, not deficit-based, interventions."
    elif firstgen == "exclude_unreliable":
        msg_firstgen = "First-generation students often benefit from navigational support. Omitting this variable could undermine equity goals."
    elif firstgen == "flag_improvement":
        msg_firstgen = "Right call"
    else:
        msg_firstgen = ""

    # --- Distance from Home ---
    distance = get_distance_choice()
    if distance == "include_as_is":
        msg_distance = "Distance correlates with homesickness and travel cost but offers limited intervention levers. Note whether actionable support exists (e.g., travel grants)."
    elif distance == "exclude_unreliable":
        msg_distance = "Ignoring Distance removes insight into geographically isolated students who may need community-building initiatives."
    elif distance == "flag_improvement":
        msg_distance = "Right call"
    else:
        msg_distance = ""

    # --- Credits After Add/Drop ---
    credits = get_credits_choice()
    if credits == "include_as_is":
        msg_credits = "Strong early signal of load management issues. Advisors can act quickly—solid choice."
    elif credits == "exclude_unreliable":
        msg_credits = "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value."
    elif credits == "flag_improvement":
        msg_credits = "Right call"
    else:
        msg_credits = ""

    # --- Live On-Campus or Commuter ---
    livecampus = get_livecampus_choice()
    if livecampus == "include_as_is":
        msg_livecampus = "Useful and actionable—commuters may need remote-friendly support. Ensure interventions respect time and travel constraints."
    elif livecampus == "exclude_unreliable":
        msg_livecampus = "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk."
    elif livecampus == "flag_improvement":
        msg_livecampus = "Right call"
    else:
        msg_livecampus = ""

    # --- Residency ---
    residency = get_residency_choice()
    if residency == "include_as_is":
        msg_residency = "Residency drives cost burden; interventions must avoid stereotyping out-of-state students as less committed."
    elif residency == "exclude_unreliable":
        msg_residency = "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups."
    elif residency == "flag_improvement":
        msg_residency = "Right call"
    else:
        msg_residency = ""

    # --- Urban / Rural / Suburban Origin ---
    origin = get_origin_choice()
    if origin == "include_as_is":
        msg_origin = "Heuristic classification may mislabel students; validate definitions or risk noisy signals."
    elif origin == "exclude_unreliable":
        msg_origin = "Campus adjustment often differs by origin. Excluding could overlook rural-to-urban transition challenges."
    elif origin == "flag_improvement":
        msg_origin = "Right call"
    else:
        msg_origin = ""

    # --- Transfer Status ---
    transfer = get_transfer_choice()
    if transfer == "include_as_is":
        msg_transfer = "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant."
    elif transfer == "exclude_unreliable":
        msg_transfer = "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support."
    elif transfer == "flag_improvement":
        msg_transfer = "Right call"
    else:
        msg_transfer = ""

    # --- Extracurricular Involvement ---
    extracurricular = get_extracurricular_choice()
    if extracurricular == "include_as_is":
        msg_extracurricular = "Self-report bias and missingness limit reliability; document caveats to avoid overstating predictive value."
    elif extracurricular == "exclude_unreliable":
        msg_extracurricular = "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright."
    elif extracurricular == "flag_improvement":
        msg_extracurricular = "Right call"
    else:
        msg_extracurricular = ""

    # --- Campus-Wi-Fi Gaming Network Participation ---
    gaming = get_gaming_choice()
    if gaming == "include_as_is":
        msg_gaming = "Correlation to retention unproven; risk of pathologising hobby behaviour. Provide theoretical justification or exclude."
    elif gaming == "exclude_unreliable":
        msg_gaming = "Sensible—no established link to academic persistence."
    elif gaming == "flag_improvement":
        msg_gaming = "Right call"
    else:
        msg_gaming = ""

    # --- Build accordion content ---
    content_detail_feedback4 = mo.vstack([
        mo.md(f"**Legacy Status:** {msg_legacy}"),
        mo.md(f"**Student Athlete Status:** {msg_athlete}"),
        mo.md(f"**First-Generation Student:** {msg_firstgen}"),
        mo.md(f"**Distance from Home:** {msg_distance}"),
        mo.md(f"**Credits After Add/Drop:** {msg_credits}"),
        mo.md(f"**Live On-Campus or Commuter:** {msg_livecampus}"),
        mo.md(f"**Residency:** {msg_residency}"),
        mo.md(f"**Urban / Rural / Suburban Origin:** {msg_origin}"),
        mo.md(f"**Transfer Status:** {msg_transfer}"),
        mo.md(f"**Extracurricular Involvement:** {msg_extracurricular}"),
        mo.md(f"**Campus-Wi-Fi Gaming Network Participation:** {msg_gaming}"),
    ])

    mo.accordion({"Detailed Feedback – Task 4": content_detail_feedback4})

@app.cell
def section_separator():
    mo.Html("""
    <hr style="border: 1px dashed black; margin-top:2.5rem; margin-bottom:3rem;">
    """)
# ------------------------------------------------------------
# End-of-Scenario Wrap-Up – Summary Table (Improved Layout)
# ------------------------------------------------------------
# ------------------------------------------------------------
# Wrap-Up – Global State & Dynamic Intro Text
# ------------------------------------------------------------
@app.cell
def wrapup_intro(
    # Task 1 getters
    get_choice, get_efc_choice, get_sai_choice, get_unmet_choice, get_merit_choice, get_pplus_choice,
    # Task 2 getters
    get_race_choice, get_gender_choice, get_age_choice, get_pronouns_choice,
    # Task 3 getters
    get_hsgpa_choice, get_tests_choice, get_midterm_choice, get_epr_choice, get_printer_choice,
    # Task 4 getters
    get_legacy_choice, get_athlete_choice, get_firstgen_choice, get_distance_choice, get_credits_choice,
    get_livecampus_choice, get_residency_choice, get_origin_choice, get_transfer_choice,
    get_extracurricular_choice, get_gaming_choice
):
    # ---- Global submit state ----
    submit_state, set_submit_state = mo.state(False)

    # ---- Helper to standardize decision ----
    def dec_label(choice):
        if choice in ["include", "include_as_is"]:
            return "Include"
        elif choice in ["flag", "flag_improvement", "audit_only"]:
            return "Flag"
        elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
            return "Exclude"
        else:
            return "No Selection"

    # ---- Collect all choices ----
    all_choices = [
        get_choice(), get_efc_choice(), get_sai_choice(), get_unmet_choice(), get_merit_choice(), get_pplus_choice(),
        get_race_choice(), get_gender_choice(), get_age_choice(), get_pronouns_choice(),
        get_hsgpa_choice(), get_tests_choice(), get_midterm_choice(), get_epr_choice(), get_printer_choice(),
        get_legacy_choice(), get_athlete_choice(), get_firstgen_choice(), get_distance_choice(), get_credits_choice(),
        get_livecampus_choice(), get_residency_choice(), get_origin_choice(), get_transfer_choice(),
        get_extracurricular_choice(), get_gaming_choice()
    ]

    # ---- Count included variables ----
    include_count = sum(1 for c in all_choices if dec_label(c) == "Include")

    # ---- Keep returning states for later use ----
    return submit_state, set_submit_state


@app.cell
def wrapup_summary_table(
    # Task 1 getters
    get_choice, get_efc_choice, get_sai_choice, get_unmet_choice, get_merit_choice, get_pplus_choice,
    # Task 2 getters
    get_race_choice, get_gender_choice, get_age_choice, get_pronouns_choice,
    # Task 3 getters
    get_hsgpa_choice, get_tests_choice, get_midterm_choice, get_epr_choice, get_printer_choice,
    # Task 4 getters
    get_legacy_choice, get_athlete_choice, get_firstgen_choice, get_distance_choice, get_credits_choice,
    get_livecampus_choice, get_residency_choice, get_origin_choice, get_transfer_choice,
    get_extracurricular_choice, get_gaming_choice
):

    def decision_label(choice):
        if choice in ["include", "include_as_is", "include_as-is"]:
            return "Include"
        elif choice in ["flag", "flag_improvement", "audit_only"]:
            return "Flag"
        elif choice in ["exclude", "exclude_unreliable", "exclude_entirely"]:
            return "Exclude"
        else:
            return "No Selection"

    grouped_rows = {
        "Regulatory Gate": [
            (decision_label(get_choice()), "Pell Status"),
            (decision_label(get_efc_choice()), "Expected Family Contribution (EFC)"),
            (decision_label(get_sai_choice()), "Student Aid Index (SAI)"),
            (decision_label(get_unmet_choice()), "Unmet Need"),
            (decision_label(get_merit_choice()), "Merit Award Amount"),
            (decision_label(get_pplus_choice()), "Pell Plus"),
        ],
        "Protected-Attribute Gate": [
            (decision_label(get_race_choice()), "Race"),
            (decision_label(get_gender_choice()), "Gender"),
            (decision_label(get_age_choice()), "Age"),
            (decision_label(get_pronouns_choice()), "Preferred Pronouns"),
        ],
        "Data-Reliability Gate": [
            (decision_label(get_hsgpa_choice()), "High-School GPA"),
            (decision_label(get_tests_choice()), "Test Scores"),
            (decision_label(get_midterm_choice()), "Mid-Term Grades"),
            (decision_label(get_epr_choice()), "Early Progress Reports"),
            (decision_label(get_printer_choice()), "Dorm-Printer Usage"),
        ],
        "Equity & Actionability Gate": [
            (decision_label(get_legacy_choice()), "Legacy Status"),
            (decision_label(get_athlete_choice()), "Student Athlete Status"),
            (decision_label(get_firstgen_choice()), "First-Generation Student"),
            (decision_label(get_distance_choice()), "Distance from Home"),
            (decision_label(get_credits_choice()), "Credits After Add/Drop"),
            (decision_label(get_livecampus_choice()), "Live On-Campus or Commuter"),
            (decision_label(get_residency_choice()), "Residency (In/Out/International)"),
            (decision_label(get_origin_choice()), "Urban / Rural / Suburban Origin"),
            (decision_label(get_transfer_choice()), "Transfer Status"),
            (decision_label(get_extracurricular_choice()), "Extracurricular Involvement"),
            (decision_label(get_gaming_choice()), "Campus-Wi-Fi Gaming Participation"),
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


# ------------------------------------------------------------
# Wrap-Up – Action Buttons (Centered Anchor Link Version + Final Feedback Title)
# ------------------------------------------------------------
@app.cell
def wrapup_buttons():
    buttons_html = """
    <div style="display:flex; justify-content:center; gap:1rem; margin-bottom:1rem;">
        <a href="#task_1" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
            Review Wave 1
        </a>
        <a href="#task_2" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
            Review Wave 2
        </a>
        <a href="#task_3" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
            Review Wave 3
        </a>
        <a href="#task_4" style="padding:6px 12px; background:#eee; border-radius:6px; text-decoration:none;">
            Review Wave 4
        </a>
    </div>
    """

    # Thick horizontal line + centered light green title
    final_feedback_html = """
    <hr style="border: 3px solid #4CAF50; margin-top:1rem; margin-bottom:1rem;">
    <div style="text-align:center; color:#4CAF50; font-size:1.5rem; font-weight:bold; margin-bottom:1rem;">
        Final Feedback
    </div>
    """

    mo.vstack([
        mo.Html(buttons_html),
        mo.Html(final_feedback_html)
    ])




# ------------------------------------------------------------
# Wrap-Up Feedback – Regulatory Gate (Improved Visual Grouping)
# ------------------------------------------------------------

@app.cell
def wrapup_feedback_regulatory(
    get_choice, get_efc_choice, get_sai_choice, get_unmet_choice, get_merit_choice, get_pplus_choice
):
    def feedback_text(var, sel):
        if var == "Pell Status":
            if sel == "include":
                return "Including Pell Status violates current federal guidance and may expose the institution to penalties. Consider aggregate reporting instead of individual-level use."
            elif sel in ["flag", "exclude"]:
                return "Right call"
        elif var == "Expected Family Contribution (EFC)":
            if sel == "include":
                return "EFC is explicitly barred under 2024 Department of Education rules; its inclusion would render the model non-compliant."
            elif sel in ["flag", "exclude"]:
                return "Right call"
        elif var == "Student Aid Index (SAI)":
            if sel == "include":
                return "SAI is sensitive financial-aid data with incomplete coverage. Using it risks privacy violations and injects missing-data bias."
            elif sel in ["flag", "exclude"]:
                return "Right call"
        elif var == "Unmet Need":
            if sel == "include":
                return "Unmet Need combines multiple restricted data points. Including it would contravene policy and amplify socioeconomic bias."
            elif sel in ["flag", "exclude"]:
                return "Right call"
        elif var == "Merit Award Amount":
            if sel == "include":
                return "Merit awards can proxy socioeconomic status and unintentionally disadvantage low-income students. Use only with a strong equity justification."
            elif sel in ["flag", "exclude"]:
                return "Right call"
        elif var == "Pell Plus":
            if sel == "include":
                return "Pell Plus directly signals Pell participation; individual-level use is restricted. Exclude or seek explicit legal clearance."
            elif sel in ["flag", "exclude"]:
                return "Right call"

    vars_choices = {
        "Pell Status": get_choice(),
        "Expected Family Contribution (EFC)": get_efc_choice(),
        "Student Aid Index (SAI)": get_sai_choice(),
        "Unmet Need": get_unmet_choice(),
        "Merit Award Amount": get_merit_choice(),
        "Pell Plus": get_pplus_choice(),
    }

    alert_flag = False
    wrong_lines = []
    correct_vars = []

    for var, sel in vars_choices.items():
        txt = feedback_text(var, sel)
        if txt and "Right call" not in txt:
            alert_flag = True
            wrong_lines.append(mo.md(f"**{var}:** {txt}"))
        else:
            correct_vars.append(var)

    # wave-level alert
    wave_alert = (
        mo.md("⚠️ **At least one restricted variable still needs your attention.**")
        if alert_flag else
        mo.md("✅ **Everything looks good in this wave!**")
    )

    correct_line = (
        mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars)}")
        if correct_vars else mo.md("")
    )

    mo.accordion(
        {"Regulatory Gate Feedback": mo.vstack([wave_alert] + wrong_lines + [correct_line])}
    )

# ------------------------------------------------------------
# Wrap-Up Feedback – Protected-Attribute Gate
# ------------------------------------------------------------
@app.cell
def wrapup_feedback_protected(get_race_choice, get_gender_choice, get_age_choice, get_pronouns_choice):
    # --- Helper to compare correct vs wrong ---
    def feedback_text_protected(var_protected, choice_protected):
        if var_protected == "Race":
            if choice_protected == "include_as_is":
                return "Using Race as a predictive feature can embed historical inequities and violate institutional policy. Retain only for bias-audit."
            elif choice_protected == "exclude_entirely":
                return "Without Race you lose the ability to audit fair outcomes across groups. Best practice is to keep it for auditing while excluding it from model training."
            elif choice_protected == "audit_only":
                return "Right call"
        elif var_protected == "Gender":
            if choice_protected == "include_as_is":
                return "Directly modelling on Gender risks discriminatory interventions. Consider audit-only retention."
            elif choice_protected == "exclude_entirely":
                return "Eliminating Gender data removes a key lens for detecting gender-based disparities as-is outputs."
            elif choice_protected == "audit_only":
                return "Right call"
        elif var_protected == "Age":
            if choice_protected == "include_as_is":
                return "Age may correlate with persistence but also with protected status (non-traditional learners). Document equity safeguards or shift to audit-only use."
            elif choice_protected == "exclude_entirely":
                return "Excluding Age erases patterns relevant to adult learners and hampers fairness checks. Audit-only use is often a balanced choice."
            elif choice_protected == "audit_only":
                return "Right call"
        elif var_protected == "Preferred Pronouns":
            if choice_protected == "include_as_is":
                return "Preferred Pronouns are not predictive of persistence and risk trivializing gender identity. Exclude or store only for awareness training, not analytics."
            elif choice_protected == "audit_only":
                return "Pronoun data lack completeness and standardization, limiting audit utility. Exclusion is usually appropriate."
            elif choice_protected == "exclude_entirely":
                return "Right call"

    # build feedback lines
    wrong_lines_protected = []
    correct_vars_protected = []
    alert_flag_protected = False

    vars_choices_protected = {
        "Race": get_race_choice(),
        "Gender": get_gender_choice(),
        "Age": get_age_choice(),
        "Preferred Pronouns": get_pronouns_choice(),
    }

    for var_protected, choice_protected in vars_choices_protected.items():
        txt_protected = feedback_text_protected(var_protected, choice_protected)
        if txt_protected and "Right call" not in txt_protected:
            alert_flag_protected = True
            wrong_lines_protected.append(mo.md(f"**{var_protected}:** {txt_protected}"))
        else:
            correct_vars_protected.append(var_protected)

    # wave-level alert
    wave_alert_protected = (
        mo.md("⚠️ **At least one restricted variable still needs your attention.**")
        if alert_flag_protected else
        mo.md("✅ **Everything looks good in this wave!**")
    )

    correct_line_protected = (
        mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars_protected)}")
        if correct_vars_protected else mo.md("")
    )

    mo.accordion({
        "Protected-Attribute Gate Feedback": mo.vstack(
            [wave_alert_protected] + wrong_lines_protected + [correct_line_protected]
        )
    })

# ------------------------------------------------------------
# Wrap-Up Feedback – Data-Reliability Gate
# ------------------------------------------------------------
@app.cell
def wrapup_feedback_reliability(
    get_hsgpa_choice, get_tests_choice, get_midterm_choice, get_epr_choice, get_printer_choice
):
    # --- Helper to compare correct vs wrong ---
    def feedback_text_reliability(var_reliability, choice_reliability):
        if var_reliability == "High-School GPA":
            if choice_reliability == "include_as_is":
                return "High-school GPAs lack standardisation; predictive value may be swamped by noise. Consider excluding or flagging for quality remediation."
            elif choice_reliability == "exclude_unreliable":
                return "Right call"
            elif choice_reliability == "flag_improvement":
                return "Right call"
        elif var_reliability == "Test Scores":
            if choice_reliability == "include_as_is":
                return "Raw Test Scores are sparse post-COVID; treating missing as zero could bias results. A submission indicator or audit flag may be safer."
            elif choice_reliability == "exclude_unreliable":
                return "Dropping Test Scores ignores a potentially strong signal for the subset who submitted. Could you retain a binary ‘submitted’ flag instead?"
            elif choice_reliability == "flag_improvement":
                return "Right call"
        elif var_reliability == "Mid-Term Grades":
            if choice_reliability == "include_as_is":
                return "Mid-Term Grades appear only for certain courses, risking departmental bias. Flag for quality improvement or exclude."
            elif choice_reliability == "exclude_unreliable":
                return "Excluding Mid-Term Grades forfeits early academic-performance insight. Could selective inclusion or data-quality work make it viable?"
            elif choice_reliability == "flag_improvement":
                return "Right call"
        elif var_reliability == "Early Progress Reports":
            if choice_reliability == "include_as_is":
                return "Sparse, faculty-dependent reporting could mislead the model. Flag for improvement or consider exclusion."
            elif choice_reliability == "exclude_unreliable":
                return "You lose a proven early-alert signal. Engage stakeholders to improve reporting rather than discard entirely."
            elif choice_reliability == "flag_improvement":
                return "Right call"
        elif var_reliability == "Dorm-Printer Usage":
            if choice_reliability == "include_as_is":
                return "Printer logs cover only a subset of students and machines, yielding noisy, biased counts. Little theoretical link to persistence."
            elif choice_reliability == "flag_improvement":
                return "Standardising printer data would require major infrastructure changes—benefit unlikely to justify cost."
            elif choice_reliability == "exclude_unreliable":
                return "Right call"

    # build feedback lines
    wrong_lines_reliability = []
    correct_vars_reliability = []
    alert_flag_reliability = False

    vars_choices_reliability = {
        "High-School GPA": get_hsgpa_choice(),
        "Test Scores": get_tests_choice(),
        "Mid-Term Grades": get_midterm_choice(),
        "Early Progress Reports": get_epr_choice(),
        "Dorm-Printer Usage": get_printer_choice(),
    }

    for var_reliability, choice_reliability in vars_choices_reliability.items():
        txt_reliability = feedback_text_reliability(var_reliability, choice_reliability)
        if txt_reliability and "Right call" not in txt_reliability:
            alert_flag_reliability = True
            wrong_lines_reliability.append(mo.md(f"**{var_reliability}:** {txt_reliability}"))
        else:
            correct_vars_reliability.append(var_reliability)

    wave_alert_reliability = (
        mo.md("⚠️ **At least one restricted variable still needs your attention.**")
        if alert_flag_reliability else
        mo.md("✅ **Everything looks good in this wave!**")
    )

    correct_line_reliability = (
        mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars_reliability)}")
        if correct_vars_reliability else mo.md("")
    )

    mo.accordion({
        "Data-Reliability Gate Feedback": mo.vstack(
            [wave_alert_reliability] + wrong_lines_reliability + [correct_line_reliability]
        )
    })

# ------------------------------------------------------------
# Wrap-Up Feedback – Equity & Actionability Gate
# ------------------------------------------------------------
@app.cell
def wrapup_feedback_equity(
    get_legacy_choice, get_athlete_choice, get_firstgen_choice, get_distance_choice,
    get_credits_choice, get_livecampus_choice, get_residency_choice, get_origin_choice,
    get_transfer_choice, get_extracurricular_choice, get_gaming_choice
):
    # --- Helper to compare correct vs wrong ---
    def feedback_text_equity(var_equity, choice_equity):
        if var_equity == "Legacy Status":
            if choice_equity == "include_as_is":
                return "Legacy Status may encode privilege and could unfairly prioritise well-connected students. Document why its predictive gain outweighs equity concerns."
            elif choice_equity == "exclude_unreliable":
                return "Right call"
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Student Athlete Status":
            if choice_equity == "include_as_is":
                return "Athlete status already triggers dedicated advising; flagging athletes again may waste resources. Ensure interventions add value."
            elif choice_equity == "exclude_unreliable":
                return "Athletes juggle academics and sport travel. Excluding this variable may hide a known risk group lacking time for coursework."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "First-Generation Student":
            if choice_equity == "include_as_is":
                return "Good call—first-gen status supports equity-minded outreach. Be sure to explain positive, not deficit-based, interventions."
            elif choice_equity == "exclude_unreliable":
                return "First-generation students often benefit from navigational support. Omitting this variable could undermine equity goals."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Distance from Home":
            if choice_equity == "include_as_is":
                return "Distance correlates with homesickness and travel cost but offers limited intervention levers. Note whether actionable support exists (e.g., travel grants)."
            elif choice_equity == "exclude_unreliable":
                return "Ignoring Distance removes insight into geographically isolated students who may need community-building initiatives."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Credits After Add/Drop":
            if choice_equity == "include_as_is":
                return "Strong early signal of load management issues. Advisors can act quickly—solid choice."
            elif choice_equity == "exclude_unreliable":
                return "Course-load changes are an actionable red flag. Excluding them weakens the model’s practical value."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Live On-Campus or Commuter":
            if choice_equity == "include_as_is":
                return "Useful and actionable—commuters may need remote-friendly support. Ensure interventions respect time and travel constraints."
            elif choice_equity == "exclude_unreliable":
                return "Housing status strongly predicts engagement. Excluding it may mask differences in retention risk."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Residency (In-State / Out-of-State / International)":
            if choice_equity == "include_as_is":
                return "Residency drives cost burden; interventions must avoid stereotyping out-of-state students as less committed."
            elif choice_equity == "exclude_unreliable":
                return "Cost differentials matter. Removing Residency could blunt financial-aid outreach to high-tuition groups."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Urban / Rural / Suburban Origin":
            if choice_equity == "include_as_is":
                return "Heuristic classification may mislabel students; validate definitions or risk noisy signals."
            elif choice_equity == "exclude_unreliable":
                return "Campus adjustment often differs by origin. Excluding could overlook rural-to-urban transition challenges."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Transfer Status":
            if choice_equity == "include_as_is":
                return "Transfer students face unique credit-articulation hurdles—actionable and equity-relevant."
            elif choice_equity == "exclude_unreliable":
                return "You dropped a key subgroup with elevated departure risk. Advisors may miss needed support."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Extracurricular Involvement":
            if choice_equity == "include_as_is":
                return "Self-report bias and missingness limit reliability; document caveats to avoid overstating predictive value."
            elif choice_equity == "exclude_unreliable":
                return "Engagement predicts belonging; consider flagging data-quality issues rather than discarding outright."
            elif choice_equity == "flag_improvement":
                return "Right call"
        elif var_equity == "Campus-Wi-Fi Gaming Network Participation":
            if choice_equity == "include_as_is":
                return "Correlation to retention unproven; risk of pathologising hobby behaviour. Provide theoretical justification or exclude."
            elif choice_equity == "exclude_unreliable":
                return "Right call"
            elif choice_equity == "flag_improvement":
                return "Right call"

    # build feedback lines
    wrong_lines_equity = []
    correct_vars_equity = []
    alert_flag_equity = False

    vars_choices_equity = {
        "Legacy Status": get_legacy_choice(),
        "Student Athlete Status": get_athlete_choice(),
        "First-Generation Student": get_firstgen_choice(),
        "Distance from Home": get_distance_choice(),
        "Credits After Add/Drop": get_credits_choice(),
        "Live On-Campus or Commuter": get_livecampus_choice(),
        "Residency (In-State / Out-of-State / International)": get_residency_choice(),
        "Urban / Rural / Suburban Origin": get_origin_choice(),
        "Transfer Status": get_transfer_choice(),
        "Extracurricular Involvement": get_extracurricular_choice(),
        "Campus-Wi-Fi Gaming Network Participation": get_gaming_choice(),
    }

    for var_equity, choice_equity in vars_choices_equity.items():
        txt_equity = feedback_text_equity(var_equity, choice_equity)
        if txt_equity and "Right call" not in txt_equity:
            alert_flag_equity = True
            wrong_lines_equity.append(mo.md(f"**{var_equity}:** {txt_equity}"))
        else:
            correct_vars_equity.append(var_equity)

    wave_alert_equity = (
        mo.md("⚠️ **At least one restricted variable still needs your attention.**")
        if alert_flag_equity else
        mo.md("✅ **Everything looks good in this wave!**")
    )

    correct_line_equity = (
        mo.md(f"✅ **No major concerns for:** {', '.join(correct_vars_equity)}")
        if correct_vars_equity else mo.md("")
    )

    mo.accordion({
        "Equity & Actionability Gate Feedback": mo.vstack(
            [wave_alert_equity] + wrong_lines_equity + [correct_line_equity]
        )
    })

@app.cell
def task_f():
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




if __name__ == "__main__":
    app.run()         