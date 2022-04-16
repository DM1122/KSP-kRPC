"""Plotting and visualization tools."""
# stdlib
import logging
from pathlib import Path

# external
import pandas as pd
import plotly
import plotly.express as px

LOG = logging.getLogger(__name__)

output_path = Path("output/images")


def line(
    df: pd.DataFrame,
    x: str,
    y: str | list[str],
    fc: str = None,
    fr: str = None,
    x_error: str = None,
    y_error: str = None,
    markers: bool = False,
    title: str = None,
    show: bool = False,
    dark: bool = False,
):
    """Plots a line plot.

    Supports up to 4D data.
    Will show plot in browser window when called. Supports plotting of multiple traces
    on the same figure. Axis and legend labels are taken from column names. LaTeX
    directives for rendering mathematical notation are enabled by encapsulating strings
    in dollar signs: "$...$". It is recommened to avoid writing LaTeX when using facets,
    as the value of the variable at the facets will not be rendered. Only supports one
    set of error data across all traces.
    Args:
        df: dataframe containing x and y data down columns.
        x: column name to treat as x coordinates of trace(s).
        y: column name(s) to treat as y coordinates of trace(s).
        fc: column name to treat as facet column of trace(s).
        fr: column name to treat as facet row of trace(s).
        x_error: column name to treat as x error of trace(s) for plotting horizontal error bars.
        y_error: column name to treat as y error of trace(s) for plotting vertical error bars.
        markers: whether to plot markers on data points.
        title: title of plot.
        show: whether to show plot.
        dark: plot in dark mode.
    Returns:
        figure object.

    """

    template = "plotly_dark" if dark else "plotly"

    fig = px.line(
        data_frame=df,
        x=x,
        y=y,
        title=title,
        error_x=x_error,
        error_y=y_error,
        markers=markers,
        facet_col=fc,
        facet_row=fr,
        template=template,
    )

    if show:
        plotly.offline.plot(fig, include_mathjax="cdn")

    return fig
