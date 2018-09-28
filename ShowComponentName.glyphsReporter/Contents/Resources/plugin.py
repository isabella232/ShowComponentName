# encoding: utf-8

from GlyphsApp import *
from GlyphsApp.plugins import *
from Foundation import NSString
import math
import traceback
from AppKit import NSColor, NSBezierPath

COLOR = 0, 0, 0.9, 0.75

class ShowComponentName ( ReporterPlugin ):

	def settings(self):
		self.menuName = u"Component Name"

	def foreground(self, layer):
		try:
			self.drawNodeDistanceText( layer )
		except:
			print traceback.format_exc()

	# def background(self, layer):
	# 	try:
	# 		try:
	# 			selection = layer.selection
	# 		except:
	# 			selection = layer.selection()
	# 		if len(selection) == 2:
	# 			x1, y1 = selection[0].x, selection[0].y
	# 			x2, y2 = selection[1].x, selection[1].y
	# 			self.drawLine((x1, y1), (x2, y2))
	# 	except:
	# 		print traceback.format_exc()

	def drawNodeDistanceText( self, layer ):
		if layer is None:
			return
		toolEventHandler = self.controller.view().window().windowController().toolEventHandler()
		toolIsTextTool = toolEventHandler.className() == "GlyphsToolText"
		toolIsToolHand = toolEventHandler.className() == "GlyphsToolHand"
		currentController = self.controller.view().window().windowController()
		if currentController:
		    if not toolIsTextTool and not toolIsToolHand:
				try:
					# scale = self.getScale()

					for eachComponent in layer.components:
						# string = NSString.stringWithString_(u"%s" % eachComponent.componentName)
						# attributes = NSString.drawTextAttributes_(NSColor.colorWithCalibratedRed_green_blue_alpha_( *COLOR ))
						# textSize = string.sizeWithAttributes_(attributes)

						cpX = eachComponent.bounds.origin.x + eachComponent.bounds.size.width/2 + 10
						cpY = eachComponent.bounds.origin.y + eachComponent.bounds.size.height/2 - 10

						cpX = cpX #* scale
						cpY = cpY #* scale

						string = eachComponent.componentName

						self.drawText( layer, string, (cpX, cpY), 10, NSColor.colorWithCalibratedRed_green_blue_alpha_( *COLOR ) )

				except:
					print traceback.format_exc()
					pass

	# def drawText( self, text, textPosition, fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_( *COLOR )):
	# 	try:
	# 		string = NSString.stringWithString_(text)
	# 		string.drawAtPoint_color_alignment_(textPosition, fontColor, 4)
	# 	except:
	# 		print traceback.format_exc()

	def drawText ( self, thisLayer, text, textPosition, fontSize, fontColor):

		try:
			thisFont = thisLayer.parent.parent
			glyphEditView = self.controller.graphicView()
			currentZoom = thisFont.currentTab.scale
			fontAttributes = { 
				NSFontAttributeName: NSFont.labelFontOfSize_( fontSize/currentZoom ),
				NSForegroundColorAttributeName: fontColor }
			displayText = NSAttributedString.alloc().initWithString_attributes_( text, fontAttributes )
			textAlignment = 4 # top left: 6, top center: 7, top right: 8, center left: 3, center center: 4, center right: 5, bottom left: 0, bottom center: 1, bottom right: 2
			glyphEditView.drawText_atPoint_alignment_( displayText, textPosition, textAlignment )

		except Exception as e:
			print e
			pass


	def RefreshView(self):
		try:
			Glyphs = NSApplication.sharedApplication()
			currentTabView = Glyphs.font.currentTab
			if currentTabView:
				currentTabView.graphicView().setNeedsDisplay_(True)
		except:
			pass


	# def getScale( self ):
	# 	try:
	# 		return self._scale
	# 	except:
	# 		return 1 # Attention, just for debugging!


	def logToConsole( self, message ):
		myLog = "Show %s plugin:\n%s" % ( self.title(), message )
		NSLog( myLog )

	# def __file__(self):
	# 	"""Please leave this method unchanged"""
	# 	return __file__
