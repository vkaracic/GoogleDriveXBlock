"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment

from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('googledrive', 'static/html'))

class GoogleDriveXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    drive_title = String(
        default="Drive title", scope=Scope.settings,
        help="Title of the drive",
        )

    drive_id = String(
        default='0B1iqp0kGPjWsNDg5NWFlZjEtN2IwZC00NmZiLWE3MjktYTE2ZjZjNTZiMDY2',
        scope=Scope.settings,
        help="ID of the drive to display",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the GoogleDriveXBlock, shown to students
        when viewing courses.
        """
        context = {
            'drive_id': self.drive_id,
            'drive_title': self.drive_title,
        }

        frag = Fragment()
        template = env.get_template('googledrive.html')
        frag.add_content(template.render(**context))
        frag.add_css(self.resource_string('static/css/googledrive.css'))

        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("GoogleDriveXBlock",
             """<googledrive drive_id="0B1iqp0kGPjWsNDg5NWFlZjEtN2IwZC00NmZiLWE3MjktYTE2ZjZjNTZiMDY2" 
             title="Example Drive" />
             """),
        ]


    def studio_view(self, context):
        """Create a fragment used to display the edit view in the Studio."""

        context = {
            'drive_id': self.drive_id,
            'drive_title': self.drive_title,
        }

        frag = Fragment()
        template = env.get_template('googledrive_edit.html')
        frag.add_content(template.render(**context))
        frag.add_css(self.resource_string("static/css/googledrive_edit.css"))
        frag.add_javascript(self.resource_string("static/js/src/googledrive_edit.js"))
        frag.initialize_js('GoogleDriveEditXBlock')
        return frag


    @XBlock.json_handler
    def studio_submit(self, data, suffix=''):
        """Called when submitting the form in Studio."""
        self.drive_title = data.get('title')
        self.drive_id = data.get('id')

        return {'result':'success'}