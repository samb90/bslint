function InterstitialMediator() as Object
	this = {

		extends: BaseMediator

		init: function () as Void
			m.addObserver("buttonResponses", "_onButtonAction")
			buttonLabels = []
			for each item in m.interstitialObject.buttons
				buttonLabels.push(item.name)
			end for
			m.setField("buttonLabels", buttonLabels)
			m.setField("theme", m.interstitialObject.theme)

			for each label in m.interstitialObject.labels.keys()
					m.setField(label, m.interstitialObject.labels[label])
			end for
		end function

		setInterstitialObject: function (interstitialObject as Object) as Void
			m.interstitialObject = interstitialObject
		end function

		_onButtonAction: function(_data as Object) as Void
			m.messageBus.dispatchEvent(m.interstitialObject.buttons[_data].event)
		end function

	}
	return this
end function
