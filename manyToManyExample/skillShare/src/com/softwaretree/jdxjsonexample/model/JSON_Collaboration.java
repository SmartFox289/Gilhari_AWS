package com.softwaretree.jdxjsonexample.model;

import org.json.JSONException;
import org.json.JSONObject;

import com.softwaretree.jdx.JDX_JSONObject;

/**
 * A shell (container) class defining a domain model object class for Employee objects 
 * based on the class JSONObject.  This class needs to define just two constructors.
 * Most of the processing is handled by the superclass JDX_JSONObject.
 * <p> 
 * @author Damodar Periwal
 *
 */
public class JSON_Collaboration extends JDX_JSONObject {

    public JSON_Collaboration() {
        super();
    }

    public JSON_Collaboration(JSONObject jsonObject) throws JSONException {
        super(jsonObject);
    }
}
