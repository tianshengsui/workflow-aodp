from virtool_workflow import step
from virtool_workflow.analysis.analysis_info import AnalysisArguments
from virtool_workflow.storage.paths import data_path, temp_path


@step
def use_analysis_args(analysis_args: AnalysisArguments):
    print(analysis_args.index_path)
