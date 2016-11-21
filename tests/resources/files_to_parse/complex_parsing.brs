function DisplayDefaultGridCommand() as Object

	this = {

		contentService: {typeOf:"ContentService"}
		configService: {typeOf: "ConfigService"}
		catalogueModel: {typeOf: "CatalogueModel"}

		execute: function (_payload={} as Object) as Void
			_node = _payload.data
			currentCatalogueCollection = m.configService.getSettingValue(Settings().CURRENT_CATALOGUE_COLLECTION)

			if currentCatalogueCollection <> Invalid and currentCatalogueCollection <> NodeTypes().UNKNOWN

				m.messageBus.dispatchEvent(Event(Actions().CLEAR_MAIN_PANEL_SET))
				m.messageBus.dispatchEvent(Event(Actions().CREATE_DEFAULT_GRID_COMPONENT, _node))

				m.configService.setSetting(Settings().CURRENT_CATALOGUE_COLLECTION, NodeTypes().UNKNOWN)
			end if

			m.catalogueModel.setViewData(_node.items[0])
			m.catalogueModel.setIndex(0)
		end function
	}
	return this

end function
